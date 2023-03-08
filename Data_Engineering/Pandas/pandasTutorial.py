import pandas as pd
import numpy as np

x = pd.Series([10, 20, 30, 40, 50])
print(x)
print(x.index)
x.index = ['A', 'B', 'C', 'D', 'E']
print(x)

data = [450, 650, 870]
Sales = pd.Series(data, index=['Don', 'Mike', 'Edwin'], name='Sales')
print(Sales.index)
print(Sales)

print(Sales.index)
print('values are {}'.format(Sales.values))
print('data type stores in series is {}'.format(Sales.dtypes))

# Accessing values using the index name
print(Sales)
print("Mike's sales {}".format(Sales['Mike']))

# Accessing values using a positional index
print(Sales[1])

# We can filter our data based on conditions we specify, we can use booleans to do this
# If we want sales greater than 500:
# Note that doing this returns booleans
print(Sales > 500)
print(Sales[Sales > 500])

sales_dict = Sales.to_dict()
print(sales_dict)

sales_ser = pd.Series(sales_dict)

# We can create a new Series from an already existing series.
# What is NaN? - Not a Number
new_sales = pd.Series(Sales, index=['Don', 'Mike', 'Sally', 'Edwin', 'Lucy'])
print(new_sales)


np.isnan(new_sales['Sally'])

print(new_sales[pd.isna(new_sales)])

print(pd.notna(new_sales))