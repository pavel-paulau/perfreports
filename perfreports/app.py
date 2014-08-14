import pymongo
from flask import Flask, render_template

app = Flask(__name__)
m = pymongo.MongoClient()


@app.route('/')
def index():
    snapshots = sorted(
        name.replace('perf', '')
        for name in m.database_names() if name.startswith('perf')
    )
    return render_template('index.html', snapshots=snapshots)

if __name__ == '__main__':
    app.run(debug=True)
