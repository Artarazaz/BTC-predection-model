import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/alirazaz/PycharmProjects/Crypto-model/BTC-predection-model/Binance_BTCUSDT_d.csv')
#print(df.head())
print(df.columns)
print(df.dtypes)
print(df.shape)

plt.figure(figsize = (10,10), dpi = 100)

x = df['Date']
y = df['Close']

plt.title('BTCUSDT Daily')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.plot(x,y)

plt.gca().invert_xaxis()

plt.show()