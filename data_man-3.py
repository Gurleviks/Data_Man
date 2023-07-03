import pandas as pd

df = pd.read_csv('/content/world_alcohol - world_alcohol.csv')

filter_list = ['value1', 'value2', 'value3']

filtered_df = df.query('Year not in @filter_list and '
                       '(`WHO region` not in @filter_list) and '
                       'Country not in @filter_list and '
                       '`Beverage Types` not in @filter_list and '
                       '`Display Value` not in @filter_list')

print(filtered_df)