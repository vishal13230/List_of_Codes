#importing libraries
import numpy as np  # array operations
import pandas as pd  # time series management
import matplotlib.pyplot as plt  # standard plotting library
#from pylab import plt
plt.style.use('ggplot')

sym = 'AAPL.O'  # our symbol
data = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv',
                   index_col=0, parse_dates=True)[sym]
data = pd.DataFrame(data)

data.tail()  # the final five rows

data.plot(figsize=(10, 6));

# vectorized calculation of the log returns
log_rets = np.log(data / data.shift(1))

# annualized average log returns
mu = log_rets.mean() * 252
mu

# annualized volatility
sigma = log_rets.std() * 252 ** 0.5
sigma

#Monte Carlo Simulation

S0 = data.iloc[-1]  # final value = initial value
sigma = sigma.values[0]  # volatility of the stock
mu = mu.values[0]  # average return
T = 1.0  # horizon 1 year
M = 252  # number of time intervals
dt = T / M  # fixed length time interval
I = 20000  # number of simulated paths

rand = np.random.standard_normal((M + 1, I))  # radnom number array
S = np.zeros_like(rand)  # array for stock prices
S[0] = S0  # all paths start at initial value
for t in range(1, M + 1):
    S[t] = S[t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * dt ** 0.5 * rand[t])
    
plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);
plt.xlim(0, M)

index = pd.date_range(start=data.index[-1], periods=M + 1, freq='B')
ax = data.plot(figsize=(10, 6), legend=False);
pd.DataFrame(S[:, :20], index=index).plot(ax=ax, legend=False);

#Option Pricing

r = 0.01  # risk-less short rate
for t in range(1, M + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * dt ** 0.5 * rand[t])
    
# vectorized payoff calculation
payoff = np.maximum(S[-1] - 110, 0)

plt.figure(figsize=(10, 6));
plt.hist(payoff, bins=50);

C0 = np.exp(-r * T) * np.sum(payoff) / I
C0  # estimated call option price