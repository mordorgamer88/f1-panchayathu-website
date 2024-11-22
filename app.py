from flask import Flask, render_template
import fastf1
import pandas as pd
from IPython.display import HTML
import matplotlib.pyplot as plt
pd. set_option('display.max_rows', None)
pd. set_option('display.max_columns', None)
pd. set_option('display.width', None)
pd. set_option('display.max_colwidth', None)
session = fastf1.get_session(2019, 'Sochi', 'Q')
session.load()
racedetail=session.results['BroadcastName'].to_string(index=False)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html',race=racedetail)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)