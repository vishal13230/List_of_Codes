import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data =pd.read_csv("pokemon.csv")
data.info()
data.corr()

#correlation map
f,ax = plt.subplots(figsize = (18, 18))
sns.heatmap(data.corr(), annot = True, linewidths = 0.5, fmt = "0.1f", ax = ax)
plt.show()

data.head(10)
data.columns
# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
data.Speed.plot(kind = "line", color = "g", label = "Speed", linewidth = 1, alpha = 0.5, grid = True, linestyle = ":")
data.Defense.plot(color = "r", label = "Defense", linewidth = 1, alpha = 0.5, grid = True, linestyle = "-.")
plt.legend(loc = "upper right")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Plot")
plt.show()

# Scatter Plot 
# x = attack, y = defense
data.plot(kind = "scatter", x = "Attack", y = "Defense", alpha = 0.5, color = "g")
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack Defense Scatter Plot")

# Histogram
# bins = number of bar in figure
data.Speed.plot(kind = "hist", bins = 50, figsize = (12,12), color = "r")
plt.show()

#create dictionary and look its keys and values
dictionary = {"spain":"madrid", "usa":"vegas"}
print(dictionary.keys())
print(dictionary.values())

# Keys have to be immutable objects like string, boolean, float, integer or tubles
# List is not immutable
# Keys are unique
dictionary["spain"] = "barcelona"
print(dictionary)
dictionary["france"] = "paris"
print(dictionary)
del dictionary["spain"]
print(dictionary)
print("france" in dictionary)
dictionary.clear()
print(dictionary)

data = pd.read_csv("pokemon.csv")
series = data["Defense"]
print(type(series))
data_frame = data[["Defense"]]
print(type(data_frame))

print(3>2)
print(3!=2)
print(True and False)
print(True or False)

x = data["Defense"] > 200
print(x)
data[x]

data[np.logical_and(data["Defense"] > 200, data["Attack"] > 100)]
data[(data["Defense"] > 200) & (data["Attack"] > 100)]




























