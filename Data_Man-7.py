import pandas as pd

df = pd.read_csv('/content/world_alcohol - world_alcohol.csv')

start_column = 'Year'
end_column = 'Display Value'
selected_data = df.loc[0:9, start_column:end_column]
print(selected_data)