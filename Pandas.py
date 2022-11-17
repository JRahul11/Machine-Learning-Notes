# Series
import numpy as np
import pandas as pd

age = pd.Series([10, 20, 30, 40], index=['age1', 'age2', 'age3', 'age4'])


# Access
index1 = age.age3
# Calling values in series
age.values
# Calling indices in series
age.index


# Filter
filter_age = age[age > 20]


# Change indexs
age.index = ['A1', 'A2', 'A3', 'A4']


# DataFrame

df = np.array([[20, 10, 8], [25, 8, 10], [27, 5, 3], [30, 9, 7]])

data_set = pd.DataFrame(df)

data_set = pd.DataFrame(df, index=['S1', 'S2', 'S3', 'S4'])

data_set = pd.DataFrame(df, index=['S1', 'S2', 'S3', 'S4'], columns=[
                        'Age', 'Grade1', 'Grade2'])

# Add a column to dataframe
data_set['Grade3'] = [9, 6, 7, 10]


data_set.loc['S2']

# data_set.loc[1][3]

data_set.iloc[1][3]

data_set.iloc[1, 3]

# : means all rows or columns
data_set.iloc[:, 2]
data_set.iloc[1, :]


# Inclusive : Exclusive
filter_data = data_set.iloc[:, 1:3]


# Drop a column
data_set.drop('Grade1', axis=1)


# Replace Element
data_set = data_set.replace(10, 12)
data_set = data_set.replace({12: 10, 9: 30})


# Head and Tail
data_set.head(3)
data_set.tail(2)


# Sort
data_set.sort_values('Grade1', ascending=True)

# axis 0 --> Rows and axis 1 --> Columns
data_set.sort_index(axis=0, ascending=False)


# Read data from CSV
data = pd.read_csv('Data_Set.csv')
