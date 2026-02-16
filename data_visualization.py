import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter

df = pd.read_csv('/Users/alirazaz/PycharmProjects/Crypto-model/BTC-predection-model/Binance_BTCUSDT_d.csv')

print("---" * 50)
print("Columns of file: \n")
for column in df.columns:
    print(column)
print("---" * 50)
print("Number of arrows: \n")
print(df.shape)
print("---" * 50)
print("Number of null values: \n")
print(df.isnull().sum())

df['Date'] = pd.to_datetime(df['Date'])
print("---" * 50)
print("Type of data in file: \n")
print(df.dtypes)

plt.fig, ax = plt.subplots()

x = df['Date']
y = df['Close']

plt.title('BTCUSDT Daily')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.plot(x,y)
plt.grid(True)

locator = AutoDateLocator(maxticks=15)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(ConciseDateFormatter(locator))

plt.gcf().autofmt_xdate()

plt.show()

plt.title("Violin show of Close column")
sns.violinplot(data=df['Close'])
plt.tight_layout()
plt.show()