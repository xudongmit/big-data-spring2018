import pandas as pd
import numpy as np
# If you started Atom from a directory other than the /week-03 directory, you'll need to change Python's working directory. Uncomment these lines and specify your week-03 path.
import os
os.chdir('E:/MIT3/BigData2018/big-data-spring2018/week-03')

# Reading a CSV with Skyhook data
df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

# We can print the first 5 rows of the dataframe
df.head()
df.dtypes
df.shape
# Number of rows
df.shape[0]
# Number of columns
df.shape[1]

df.columns
type(df.columns)

df.cat_name

df.count

df['count']

df.lat.unique()

df_multipleColumns = df[['hour', 'cat', 'count']]
df_multipleColumns.head()

df['hour'] == 158

time = df[df['hour'] == 158]
time.head
time.shape

df[(df['hour'] == 158) & (df['count'] > 50)]

bastille = df[df['date'] == '2017-07-14']
bastille.head(2)

bastille_enthusiasts = bastille[bastille['count'] > bastille['count'].mean()]
bastille_enthusiasts.head(2)

bastille_enthusiasts['count'].describe()

df.groupby('date')['count'].describe()
# group by multiple columns. Let's calculate summary statistics for the count column for each hour of each day!
df.groupby(['date', 'hour'])['count'].describe()

#You can save these as variables and cast them to strings.

# create min, max, and mean
max_count = df['count'].max()
min_count = df['count'].min()
mean_count = df['count'].mean()

# print out some results
print(f"Maximum number of GPS pings: {max_count}")
print(f"Minimum number of GPS pings: {min_count}")
print(f"Average number of GPS pings: {mean_count}")

# Exercise
# Calculate the minimum value and maximum value of the count column to find the hour with the highest and lowest numbers of GPS pings. You'll want to group by hour.
num_pings = df.groupby('hour')['count'].sum()
df_num_pings_byhour = pd.DataFrame(num_pings)
df_num_pings_byhour.head()
df_num_pings_byhour[df_num_pings_byhour['count']==df_num_pings_byhour['count'].max()]
df[df['count'] == df['count'].max()]

# Exercise:
# Get the average number of GPS pings per hour across the whole dataset.
avg_num_pings = df.groupby('hour')['count'].mean()
avg_num_pings

# This line lets us plot in Atom
import matplotlib
# This line allows the results of plots to be displayed inline with our code.
%matplotlib inline

day_hours = df[df['date'] == '2017-07-02'].groupby('hour')['count'].sum()
day_hours.plot()

df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

df['date'].head


df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
# for every date, add 1 weekday (by default Sunday is 6 Monday is 0), now Monday is 1, Sunday is 7
df['weekday'].replace(7, 0, inplace = True)
# now Sunday is 0

# How to select 24 hour subset for 1 day (more than 24 hour is clearly wrong)
# df[df['date'] == '2017-07-10'].groupby('hour')['count'].sum()
for i in range(0, 168, 24): # loop over the entire week (168 hours) by the step of 24 hour (by day)
  j = range(0,168,1)[i - 5] # i-5: switch to Greenwich time;
  # extract the start hour of every weekday, avoid the -5 by wrapping it into the 0-168 range (thus, -5 is 163)
  # basic idea of this data cleaning: drop the observations with the hour value out of the hour window of the certain day
  if (j > i): # In the iteration, i=0,24,48,72,96,120,144, meanwhile j=163,19,43,67,91,115,139; the first case is one special case: the day's hour window is [0,24) for local time, [163-0),[0-19) for Greenwich time. So drop the observation with the hour in [19,163) （i=0, j=163）

  # In other cases, i.e. the second day, hour window is [24,48) for local and [19,43) for Greenwich, drop the observation with the hour in [43,168] and [0,19) (i=24,j=19)
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    ( (df['hour'] < j) & (df['hour'] > i + 18) ) |
    ( (df['hour'] > i + 18 ) & (df['hour'] < j) )
    )
    ].index, inplace = True)
  else:
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    (df['hour'] < j) | (df['hour'] > i + 18 )
    )
    ].index, inplace = True)

df.shape
