# Preprocessing

import pandas as pd

# Import DataSet
data_set1 = pd.read_csv('Data_Set.csv')

# Set a Header
data_set2 = pd.read_csv('Data_Set.csv', header=2)

# Rename a Column
data_set3 = data_set2.rename(columns={'Temperature':'Temp'})

# Remove a Column
data_set4 = data_set3.drop('No. Occupants', axis=1)

data_set3.drop('No. Occupants', axis=1, inplace=True)

# Remove a Row
data_set5 = data_set4.drop(2, axis=0)

# Reset the Index
data_set6 = data_set5.reset_index(drop=True)

# Describe a dataset
data_set6.describe()

# Minimun Number
min_item = data_set6['E_Heat'].min()
# Locate Min Number
data_set6['E_Heat'][data_set6['E_Heat'] == min_item]

#  Replace a Cell
data_set6['E_Heat'].replace(-4, 21, inplace=True)


"""
Covariance
"""
data_set6.cov()

import matplotlib.pyplot as plt
import seaborn as sn

sn.heatmap(data_set6.corr())
plt.show()


"""
Missing Values
"""

data_set6.info()

import numpy as np
data_set7 = data_set6.replace('!', np.NaN)

data_set7.info()

data_set7 = data_set7.apply(pd.to_numeric)

data_set7.isnull()

# Drop one row
data_set7.drop(13, axis=0, inplace=True)

# Drop all rows which contains NaN
data_set7.dropna(axis=0, inplace=True)

# Replace NaN with the last cell's value
data_set8 = data_set7.fillna(method='ffill')
# Replace NaN with the later cell's value
data_set8 = data_set7.fillna(method='bfill')

# Replace NaN with Mean of the Column
from sklearn.impute import SimpleImputer
m_var = SimpleImputer(missing_values=np.nan, strategy='mean')
m_var.fit(data_set7)
data_set9 = m_var.transform(data_set7)



"""
Outlier Detection
"""
data_set8.boxplot()

data_set8['E_Plug'].quantile(0.25)
data_set8['E_Plug'].quantile(0.75)

# Q1 = 21.25
# Q2 = 33.75
# IQR = 33.75 - 21.25 = 12.5

# Mild Outlier
#Lower Bound = Q1 - 1.5*IQR = 21.25 - 1.5*12.5 = 2.5
#Upper Bound = Q3 + 1.5*IQR = 33.75 + 1.5*12.5 = 52.5

# Extreme Outlier
#Lower Bound = Q1 - 3*IQR = 21.25 - 3*12.5 = -16.25
#Upper Bound = Q3 + 3*IQR = 33.75 + 3*12.5 = 71.25

data_set8['E_Plug'].replace(120, 42, inplace=True)



"""
Concatenation
"""

new_col = pd.read_csv('Data_New.csv')

# Concate by column side
data_set10 = pd.concat([data_set8, new_col], axis=1)



"""
Dummy Variables
"""
data_set10.info()

data_set11 = pd.get_dummies(data_set10)

data_set11.info()



"""
Normalization
"""
from sklearn.preprocessing import minmax_scale, normalize   

# First Method: Min Max Scale

data_set12 = minmax_scale(data_set11, feature_range=(0,1))
print(data_set12)

data_set13 = normalize(data_set11, norm='l2', axis=0)

# axis = 0  for normalizing features / axis = 1 for normalizing each sample


# Final Processed DataSet
data_set14 = pd.DataFrame(data_set13, columns=['Time','E_Plug','E_Heat','Price','Temp','OffPeak','Peak'])