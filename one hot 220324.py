import pandas
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pandas.DataFrame({'robot': lst})

unique_values = data['robot'].unique()

one_hot = pandas.DataFrame()

for value in unique_values:
    one_hot[f'{value}_isPresent'] = (data['robot'] == value).astype(bool)

print(one_hot.head())