import pandas as pd

data = pd.read_csv('/content/world_alcohol - world_alcohol.csv')
filtered_data = data[data['Display Value'].between(0.5, 2.50)]
print(filtered_data)