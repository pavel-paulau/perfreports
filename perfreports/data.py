import sys

import pandas as pd
import pymongo
from pymongo.errors import ConnectionFailure

try:
    m = pymongo.MongoClient()
except ConnectionFailure:
    sys.exit('MongoDB is not running... exiting.')


def get_all_snapshots():
    return sorted(
        name.replace('perf', '')
        for name in m.database_names() if name.startswith('perf')
    )


def get_data_paths(snapshot):
    snapshot = 'perf' + snapshot

    data_paths = []
    for source in m[snapshot].collection_names():
        if source != 'system.indexes':
            for metric in m[snapshot][source].find().distinct(key='m'):
                data_paths.append('{}:{}'.format(source, metric))

    return data_paths


def get_series(snapshot, data_path):
    snapshot = 'perf' + snapshot

    source, metric = data_path.split(':')

    series = pd.Series({
        sample['ts']: sample['v']
        for sample in m[snapshot][source].find({'m': metric}, {'v': 1, 'ts': 1})
    })
    series.dropna()
    series.index = series.index.astype('uint64')
    series.rename(lambda x: x - series.index.values.min(), inplace=True)
    series.rename(lambda x: x / 10 ** 9, inplace=True)  # ns -> s

    return series
