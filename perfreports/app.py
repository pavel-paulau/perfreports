import os
import re

import pymongo
from flask import Flask, render_template, send_from_directory

from perfreports import data
from perfreports.constants import LABELS
from perfreports.plotter import plot

app = Flask(__name__)
m = pymongo.MongoClient()


@app.route('/')
def index():
    snapshots = data.get_all_snapshots()
    return render_template('index.html', snapshots=snapshots)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


def generate_filename(snapshot, source, metric):
    filename = '_'.join((snapshot, source, metric))
    filename = re.sub(r'[\[\]/\\:\*\?\"<>\|& ]', '', filename)
    return 'perfreports/static/charts/{}.png'.format(filename)


@app.route('/<snapshot>')
def report(snapshot):
    meta = []

    for data_path in data.get_data_paths(snapshot=snapshot):
        source, metric = data_path.split(':')
        fname = generate_filename(snapshot, source, metric)
        series = data.get_series(snapshot=snapshot, data_path=data_path)
        label = LABELS.get(metric, metric)
        plot(series=series, ylabel=label, fname=fname)

        meta.append(('{} : {} : {}'.format(source, metric, label),
                     fname.replace('perfreports', '')))

    return render_template('report.html', meta=meta)


if __name__ == '__main__':
    app.run(debug=True)
