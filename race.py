import fastf1
import pandas as pd
import matplotlib.pyplot as plt
pd. set_option('display.max_rows', None)
pd. set_option('display.max_columns', None)
pd. set_option('display.width', None)
pd. set_option('display.max_colwidth', None)
session = fastf1.get_session(2019, 'Monza', 'Q')
session.load()
print (session. results['TeamName'])