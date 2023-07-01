import pandas as pd

df = pd.read_csv('/content/world_alcohol - world_alcohol.csv')

filtered_df = df[1::5]
print(filtered_df)