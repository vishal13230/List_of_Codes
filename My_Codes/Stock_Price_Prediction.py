import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR


data = pd.read_csv("HDFC.BO.csv")
df_date = data.loc[:, "Date"]
df_date = pd.DataFrame.from_dict(df_date)

df_date = pd.concat([df_date.Date.str.split('-', expand=True)], axis=1)

df_date.iloc[:,0] = pd.to_numeric(df_date.iloc[:,0])
df_date.iloc[:,1] = pd.to_numeric(df_date.iloc[:,1])
df_date.iloc[:,2] = pd.to_numeric(df_date.iloc[:,2])

df_date.columns = ['year', 'month', 'date']

df_date['final'] = 10000*df_date['year'] + 100* df_date['month'] + df_date['date']
df_date['final'] = np.reshape(df_date['final'], len(df_date['final']), 1)

df_price = data.loc[:, "Adj Close"]

svr_lin = SVR(kernel = 'linear')
svr_poly = SVR(kernel = 'poly', degree = 2)
svr_rbf = SVR(gamma = 0.1)


svr_lin.fit(df_date['final'], df_price)
svr_poly.fit(df_date['final'], df_price)
svr_rbf.fit(df_date['final'], df_price)

plt.scatter(df_date['final'], df_price, color = 'blue', label = 'Data')
plt.plot(df_date['final'], svr_rbf.predict(df_date['final']), color = 'red', label = 'RBF model')
plt.plot(df_date['final'], svr_lin.predict(df_date['final']), color = 'green', label = 'Linear model')
plt.plot(df_date['final'], svr_poly.predict(df_date['final']), color = 'pink', label = 'Polynomial model')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Support Vector Regression')
plt.legend()
plt.show()




