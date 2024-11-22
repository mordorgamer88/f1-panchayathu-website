from flask import Flask, render_template
import fastf1
import pandas as pd
from IPython.display import HTML
import matplotlib.pyplot as plt
pd. set_option('display.max_rows', None)
pd. set_option('display.max_columns', None)
pd. set_option('display.width', None)
pd. set_option('display.max_colwidth', None)
session = fastf1.get_event_schedule(2019)


print(session)
