import pandas as pd
bank_stocks = pd.read_pickle("all_banks.pickle")
bank_stocks.xs('Close',axis=1,level=1).plot(figsize=(12,5))