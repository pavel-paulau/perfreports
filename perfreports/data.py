import pandas as pd
import requests


BASE_URL = 'http://127.0.0.1:8080/'


session = requests.session()


def snapshots(*args):
    return session.get(url='{}'.format(BASE_URL, *args)).json()


def sources(*args):
    return session.get(url='{}/{}'.format(BASE_URL, *args)).json()


def metrics(*args):
    return session.get(url='{}/{}/{}'.format(BASE_URL, *args)).json()


def raw_data(*args):
    return session.get(url='{}/{}/{}/{}'.format(BASE_URL, *args)).json()


def summary(*args):
    return session.get(url='{}/{}/{}/{}/summary'.format(BASE_URL, *args)).json()


def get_data_paths(snapshot):
    data_paths = []
    for source in sources(snapshot):
        for metric in metrics(snapshot, source):
            data_paths.append((source, metric))
    return data_paths


def get_series(snapshot, source, metric):
    series = pd.Series(raw_data(snapshot, source, metric))
    series.index = series.index.astype('uint64')
    series.rename(lambda x: x - series.index.values.min(), inplace=True)
    series.rename(lambda x: x / 10 ** 9, inplace=True)  # ns -> s

    return series
