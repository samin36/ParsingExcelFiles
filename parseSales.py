import pandas as pd
from datetime import datetime as dt

data = pd.read_csv('./Sales_Data/Sales_Merged.csv')

data = data[(data['Product'].notnull()) & ~(
    data['Quantity Ordered'] == 'Quantity Ordered')]

data['Quantity Ordered'] = data['Quantity Ordered'].astype(int)
data['Price Each'] = data['Price Each'].astype(float)

data['Sale'] = (data['Quantity Ordered']) * (data['Price Each'])

data['Month'] = data['Order Date'].map(
    lambda date: dt.strptime(date, '%m/%d/%y %H:%M').strftime('%B'))

# data['City'] = data['Purchase Address'].map(
#     lambda address: f"{address.split(', ')[1]} ({address.split(', ')[2].split()[0]})")

# data = data[data['Order ID'].duplicated(keep=False)]

# data['Grouped By'] = data.groupby(by=['Order ID'])['Product'].transform(
#     lambda product: ', '.join(product))

data = data.groupby(by=['Month']).sum().sort_values(
    by=['Sale'], ascending=False)
print(data)
