import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from itertools import cycle, islice

# This line lets us plot on our ipython notebook
%matplotlib inline
plt.style.use('ggplot')
# Read the data
df_voters = pd.read_table('E:/MIT3/BigData2018/big-data-spring2018/week-03/data/CENTRE_FVE_20170123.csv', sep=',',low_memory=False)
df_voters.head()
# View the unique values in column 12
df_voters['12'].unique()
# Your code here
grouped = df_voters.groupby('12') # Group by party registrations
summed = grouped['12'].count() # Get counts of each group
summed.sort_values(inplace=True, ascending=False)
df_summed = summed.to_frame()
df_summed.columns = ['NUMBER']
df_summed.index.names = ['PARTY']
df_summed

df_summed.plot.bar(legend=True)
df_summed[(df_summed.index != 'D') & (df_summed.index != 'R')]

parties = ['Democrat', 'Republican', 'Other']
values = np.array([df_summed[(df_summed.index == 'D')].NUMBER.item(),df_summed[(df_summed.index == 'R')].NUMBER.item(),df_summed[(df_summed.index != 'D') & (df_summed.index != 'R')].NUMBER.sum()])


df_parties = pd.DataFrame(values,index = parties,columns=list('N'))
df_parties


# Problem 2: Plot this as a bar chart, using red for Republican, blue for Democrat, and yellow for other.
colors = {'Democrat':'b','Republican':'r','Other':'y'}
p2 = df_parties['N'].plot(kind = 'barh',color = [colors[i] for i in df_parties.index])

# Problem 3: For this next question, implement the above. We want to compare how the number of voter registrations to election results for one precinct (PRECINCT 42). Create a bar chart that has two bars each for category (Democrat, Republican, and Other). One of the bars will represent the number of registered voters to that party, and the second bar representing the count of results (ie how many people actually voted for that parties candidate) for each group

## 27	Precinct Code == 42

# Difference between registered voters to the party and results.
# Add your code below:

# Read Election Results data and create a table for Precinct 42
df_precinct_result = pd.read_table('E:/MIT3/BigData2018/big-data-spring2018/week-03/data/centrecounty_precinct_results_nov2016.csv', sep=',',low_memory=False)
df_precinct_result.head()
df_prec42_result = df_precinct_result[(df_precinct_result['PrecNo']==42)]
df_prec42_result = df_prec42_result.loc[df_prec42_result['Contest'] == 'PRESIDENTIAL ELECTORS']

# Calculate the numbers for Republic/Democrat/Other
## Group by parties
Prec42_vote_grouped = df_prec42_result.groupby('Party').sum()
vote_count = Prec42_vote_grouped['Count']
df_Prec42_vote_summed = vote_count.to_frame()
df_Prec42_vote_summed
## Get the vote count
DEM_v = df_Prec42_vote_summed[(df_Prec42_vote_summed.index =='DEMOCRATIC')].Count.item()
REP_v = df_Prec42_vote_summed[(df_Prec42_vote_summed.index =='REPUBLICAN')].Count.item()
OTH_v = df_Prec42_vote_summed[(df_Prec42_vote_summed.index !='DEMOCRATIC') & (df_Prec42_vote_summed.index !='REPUBLICAN')].Count.sum()
values_vote = np.array([int(DEM_v),int(REP_v),int(OTH_v)])
### Build the dataframe
values_vote
df_Parties_Prec42_vote = pd.DataFrame(values_vote, index=['DEMOCRATIC','REPUBLICAN','OTHER'],columns=['Count_vote'])
df_Parties_Prec42_vote
# Read Voter Registration data and create a table for Precinct 42
df_prec42_reg = df_voters[df_voters['27']==42]
df_prec42_reg.head()
# Calculate the numbers for Republic/Democrat/Other
Prec42_reg_grouped = df_prec42_reg.groupby('12')
Prec42_reg_summed = Prec42_reg_grouped['12'].count() # Get counts of each group
Prec42_reg_summed.sort_values(inplace=True, ascending=False)
df_Prec42_reg_summed = Prec42_reg_summed.to_frame()
df_Prec42_reg_summed .columns = ['Count']
df_Prec42_reg_summed .index.names = ['PARTY']
values_reg = np.array([df_Prec42_reg_summed[(df_Prec42_reg_summed.index == 'D')].Count.item(),df_Prec42_reg_summed[(df_Prec42_reg_summed.index == 'R')].Count.item(),df_Prec42_reg_summed[(df_Prec42_reg_summed.index != 'D') & (df_Prec42_reg_summed.index != 'R')].Count.sum()])
df_Parties_Prec42_reg = pd.DataFrame(values_reg, index=['DEMOCRATIC','REPUBLICAN','OTHER'],columns=['Count_reg'])
df_Parties_Prec42_reg

# Join the two tables
df_Prec42_compare = df_Parties_Prec42_reg.join(df_Parties_Prec42_vote)
df_Prec42_compare
# Plot the dataset
plt.figure();
p3 = df_Prec42_compare.plot(kind = 'barh',alpha = 0.5)
# Part 2 - Scatterplotting
# Now we will use the precinct_centroids file provided to display the geographical location of the centroid of each precinct, plot them in a scatterplot, then size the points in the scatterplot according to the number of votes.

# First, load the CSV.

df_precinct_locations = pd.read_table('E:/MIT3/BigData2018/big-data-spring2018/week-03/data/center_county_precinct_centroids.csv', sep=',', low_memory=False)
df_precinct_locations.head()

# Now that we have a new DataFrame for each precinct and the geographical location of its centroid, we can use lat/lon values to create a scatter plot. We can even vary their size based on the variables or criteria we set. If variation across precincts is not that big, we can use a log function to better visualize it on our plot. Numpy has a quick log implementation:

# Problem 4: Using the above example, and the documentation on scatterplots, create two scatterplots using longitude and latitude X and Y locations, one showing percentage of vote for Trump, and other percentage of vote for Clinton. Make the Trump dots colored red, and Clinton blue.




def VotePercentagePlot(data, Locations, Contest, Candidate, Color):
    df = data.loc[data['Contest'] == Contest]
    df_candidate = df.loc[df['Candidate'] == Candidate]

    df_Pct = pd.DataFrame({'Percentage':df_candidate.PctCnt,'PrecNo':df_candidate.PrecNo.astype(int)})
    df_Pct.index = df_candidate.PrecNo.astype(int)

    Locations = Locations[['X','Y','Precinct']]
    Locations.index = Locations['Precinct'].astype(int)

    df_merged = pd.merge(df_Pct, Locations,left_on = 'PrecNo', right_on = 'Precinct')

    s = np.log(df_merged['Percentage']/100)
    plt.figure();
    p4 = plt.scatter(df_merged['X'],df_merged['Y'] ,s=-s*500, alpha = 0.2, color = Color)
    plt.show()


    #return df_merged

s = np.log(df_merged['Percentage']/100)


plt.scatter(df_merged['X'],df_merged['Y'] ,s=-s*500,alpha = 0.1)

# Map 1: Votes for Trump
# Add your code below:
data = df_precinct_result
Locations = df_precinct_locations

VotePercentagePlot(data, Locations, 'PRESIDENTIAL ELECTORS', 'DONALD J TRUMP,  PRESIDENT','r')

# Map 2: Votes for Clinton
# Add your code below:
VotePercentagePlot(data, Locations, 'PRESIDENTIAL ELECTORS', 'HILLARY CLINTON,  PRESIDENT','b')
