# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R82baBoxES27QgJ382OncR0c4HSLmoqR
"""

import pandas as pd
data = pd.read_csv('/content/world_alcohol - world_alcohol.csv')

filtered_data = data[data.index % 10 == 0]
print(filtered_data)