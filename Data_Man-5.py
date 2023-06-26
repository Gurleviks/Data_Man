import pandas as pd
data = pd.read_csv('/content/world_alcohol - world_alcohol.csv')

wine_cons = (data['Beverage Types'] == 'Wine') & (data['Display Value'] > 2)
count_gt_2 = wine_cons.sum()

print(count_gt_2)