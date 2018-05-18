# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# remove warnings
import warnings
warnings.filterwarnings('ignore')

# important imports

import pandas as pd
pd.options.display.max_columns = 100
import matplotlib
#from matplotlib import pyplot as plt
matplotlib.style.use('ggplot')
#pd.options.display.max_rows = 100


importData_df = pd.read_csv("Imports1.csv")
print(importData_df)

#train_df = importData_df.dropna()

