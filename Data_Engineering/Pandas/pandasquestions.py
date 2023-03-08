import pandas as pd
#Assignment:
# Pre-defined lists
country = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drives_right =[True, False, False, False, True, True, True]
cars_per_cap = [809, 731, 588, 18, 200, 70, 45]
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
#step1: Create dictionary my_dict with three key:value pairs: my_dict

mydict = {
    'country':country,
    'drives_right':drives_right,
    'cars_per_cap':cars_per_cap
}

# #step2 Build a DataFrame cars from my_dict: cars

df = pd.DataFrame(data=mydict)

print(df)
# #step3 print cars

cars = df['cars_per_cap']
print(cars)

# #step4 specify the row labels of cars

mydict2 = {
    'country':country,
    'drives_right':drives_right,
    'cars_per_cap':cars_per_cap,
    'row_labels': row_labels
}
df2 = pd.DataFrame(data=mydict2)
print(df2)

df2.set_index('row_labels', inplace = True)
print(df2)

# #step5 print cars again

print(df2['cars_per_cap'])

# #step6 Print out country column as Pandas Series

x = df2['country'].tolist()

print(pd.Series(x))

# #step7 Print out country column as Pandas DataFrame

df3 = pd.DataFrame(x)
print(df3)

# #step8 Print out DataFrame with country and drives_right columns

y = df2.loc[:,['country', 'drives_right']]
print(y)

# #step9 Print out first 3 observations

print(y[:4])

# #step10 Print out fourth, fifth and sixth observation

print(y[3:7])

# #step11 Print out observation for Japan

print(y[y.country=='Japan'])
# #step12 Print out observations for Australia and Egypt

df5 = y.loc[(y['country'] == 'Australia') | (y['country'] == 'Egypt')]
y.loc['']
print(df5)

cars[cars.country.isin(["Australia","Egypt"])]

# #step13 Print out drives_right value of Morocco

x = y.loc['MOR', 'drives_right']
print(x)
