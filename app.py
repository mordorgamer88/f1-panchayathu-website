from flask import Flask, render_template
import fastf1
import pandas as pd
import matplotlib.pyplot as plt
pd. set_option('display.max_rows', None)
pd. set_option('display.max_columns', None)
pd. set_option('display.width', None)
pd. set_option('display.max_colwidth', None)
session = fastf1.get_session(2019, 'Monza', 'Q')
session.load()
racedetail=[

       pd.DataFrame({'teamname':[session.results['TeamName']]})

]
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html',race=racedetail)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)