import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl
import datetime as dt
import math
import sklearn as sk
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LinearRegression
my_df = quandl.get("BSE/BOM533107")
my_df['date'] = my_df.index
my_df['year'] = pd.DatetimeIndex(my_df['date']).year
my_df = my_df[my_df['year'] > 2016]

#print(my_df.head())
#my_df.describe()
my_df.columns
my_df.info()
my_df = my_df[["Open", "High", "Low", "Close", "No. of Shares"]]
my_df["HL_Perct"] = (my_df["High"] - my_df["Low"])/my_df["Low"] * 100
my_df["Perct_chg"] = (my_df["Close"] - my_df["Open"])/my_df["Open"] * 100
my_df = my_df[["Close", "HL_Perct", "Perct_chg", "No. of Shares"]]
#print(my_df.head())
my_df = my_df.iloc[4:]

forecast_col = "Close"
my_df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(0.001 * len(my_df)))
#print(forecast_out)
my_df["label"] = my_df[forecast_col].shift(- forecast_out)

print(my_df.head())

my_df.dropna(inplace = True)
print(my_df.tail())

#feature Skelling
X = np.array(my_df.drop(["label"], 1))
y = np.array(my_df["label"])
X = preprocessing.scale(X)
my_df.dropna(inplace = True)
y = np.array(my_df["label"])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

classifier = LinearRegression()
model = classifier.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = classifier.score(X_test, y_test)
print(accuracy)
plt.scatter(y_test,predictions)
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.show()





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl
import datetime as dt
import math
import sklearn as sk
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LinearRegression
my_df = quandl.get("BSE/BOM533107")
my_df['date'] = my_df.index
my_df['year'] = pd.DatetimeIndex(my_df['date']).year
my_df = my_df[my_df['year'] > 2019]


#print(my_df.head())
#my_df.describe()
my_df.columns
my_df.info()
my_df = my_df[["Open", "Close", "No. of Shares"]]



my_df.dropna(inplace = True)

#feature Skelling
X = np.array(my_df.drop(["Close"], 1))
y = np.array(my_df["Close"])
X = preprocessing.scale(X)
my_df.dropna(inplace = True)
y = np.array(my_df["Close"])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

classifier = LinearRegression()
model = classifier.fit(X_train, y_train)



predict_today = model.predict('55.5', )

predictions = model.predict(X_test)
accuracy = classifier.score(X_test, y_test)
print(accuracy)
plt.scatter(y_test,predictions)
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.show()
















