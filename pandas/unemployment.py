import requests
import pandas as pd
import matplotlib.pyplot as plt

# US civilian unemployment rate
url = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
 

data = pd.read_csv(url, index_col=0, parse_dates=True) 
data['2006':'2018'].plot()
plt.show()