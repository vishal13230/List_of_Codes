# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:30:44 2022

@author: Vishal
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use("classic")

stocks = ["WMT"]

start_date = "2011-01-01"
end_date = "2021-01-01"

data = yf.download(stocks, start=start_date, end=end_date, progress=False)["Adj Close"]
data.head()
daily_returns = (data/data.shift(1)) - 1

daily_returns.hist(bins=100)
plt.show()