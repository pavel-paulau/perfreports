import os
import re

from flask import render_template, send_from_directory

from perfreports import app
from perfreports import data
from perfreports.constants import LABELS
from perfreports.plotter import plot


@app.route('/')
def index():
    snapshots = data.snapshots()
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

    for source, metric in data.get_data_paths(snapshot=snapshot):
        label = LABELS.get(metric, metric)
        fname = generate_filename(snapshot, source, metric)

        if not os.path.isfile(fname):
            series = data.get_series(snapshot, source, metric)
            plot(series=series, ylabel=label, fname=fname)

        chart_title = ' : '.join((source, label))
        meta.append((chart_title, fname.replace('perfreports', '')))

    return render_template('report.html', meta=meta)
