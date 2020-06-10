import pandas as pd

data = pd.read_excel('orders.xls')

data = data.groupby(by=['Order ID']).sum()
print(data.head(10))
