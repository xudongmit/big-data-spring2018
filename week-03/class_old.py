import pandas as pd
import numpy as np

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['Joey', 'Jeremy', 'Jenny']

# View dataframe
df

# Assign a new column to df called 'age' with a list of ages
df.assign(age = [28, 33, 27])

# We are reading a CSV with election data
df = pd.read_table('E:/MIT3/BigData2018/big-data-spring2018/week-03/data/centrecounty_precinct_results_nov2016.txt', sep=',')

# We can print the first 5 rows of the df
df.head()

df.dtypes

df.shape
df.columns
df_multipleColumns = df[['Contest','PrecNo', 'Count']]
df_multipleColumns.head()
df['PrecNo'] == 1

df_precinct1 = df[df['PrecNo'] == 1]
df_precinct1.head()

df[(df['PrecNo'] < 8) & (df['PrecNo'] > 5)]

df_pres = df.loc[df['Contest'] == 'PRESIDENTIAL ELECTORS']
df_pres

df_clinton = df_pres.loc[df_pres['Candidate'] == 'HILLARY CLINTON,  PRESIDENT']
df_clinton.head()
df_pres['Candidate'].unique()
df_clinton.PctCnt > 50
df_clinton.Count.sum()
df_pres.groupby('Candidate').Count.sum()
df_pres.groupby(['PrecNo','Candidate']).Count.sum()
df_clinton['Count'].max()
# create min, max, and mean
max_clinton = df_clinton['Count'].max()
min_clinton = df_clinton['Count'].min()
mean_clinton = df_clinton['Count'].mean()

# print out some results
print("Highest precinct vote total for Clinton: " + str(max_clinton))
print("Lowest precinct vote total for Clinton: " + str(min_clinton))
print("Mean precinct vote total for Clinton: " + str(mean_clinton))

df_clinton.loc[df['PctCnt'] == df_clinton['PctCnt'].max()]

df_clinton.loc[df['PctCnt'] == df_clinton['PctCnt'].min()]
