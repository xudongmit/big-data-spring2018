# Problem Set 3: Scraping and Cleaning Twitter Data

Now that you know how to scrape data from Twitter, let's extend the exercise a little so you can show us what you know. You will set up the scraper, clean the resulting data, and visualize it. Make sure you get your own Twitter key (AND make sure that you don't accidentally push it to GitHub); careful with your `.gitignore`.

## Graphic Presentation

Make sure to label all your axes and add legends and units (where appropriate)! Think of these graphs as though they were appearing in a published report for an audience unfamiliar with the data.

## Don't Work on Incomplete Data!

One of the dangers of cleaning data is that you inadvertently delete data that is pertinent to your analysis. If you find yourself getting strange results, you can always run previous portions of your script again to rewind your data. See the section called 'reloading your Tweets in the workshop.

## Deliverables

### Push to GitHub

1. A Python script that contains your scraper code in the provided submission folder. You can copy much of the provided scraper, but you'll have to customize it. This should include the code to generate two scatterplots, and the code you use to clean your datasets.
2. Extra Credit: A Python script that contains the code you used to scrape Wikipedia with the BeautifulSoup library.

### Submit to Stellar

1. Your final CSV files---one with no search term, one with your chosen search term---appropriately cleaned.
2. Extra Credit: A CSV file produced by your BeautifulSoup scraper.

## Instructions

### Step 1


Using the Twitter REST API, collect at least 80,000 tweets. Do not specify a search term. Use a lat/lng of `42.359416,-71.093993` and a radius of `5mi`. Note that this will probably take 20-30 minutes to run.
#### Solution.
```Python
import jsonpickle
import tweepy
import pandas as pd
import os
os.chdir('e:/MIT3/BigData2018/big-data-spring2018/week-04')
from twitter_keys import api_key, api_secret

auth = tweepy.AppAuthHandler(api_key, api_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def auth(key, secret):
	auth = tweepy.AppAuthHandler(key, secret)
	api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
	# Print error and exit if there is an authentication error
	if (not api):
		print ("Can't Authenticate")
		sys.exit(-1)
	else:
		return api

api = auth(api_key, api_secret)

def parse_tweet(tweet):
	p = pd.Series()
	if tweet.coordinates != None:
		p['lat'] = tweet.coordinates['coordinates'][0]
		p['lon'] = tweet.coordinates['coordinates'][1]
	else:
		p['lat'] = None
		p['lon'] = None
	p['location'] = tweet.user.location
	p['id'] = tweet.id_str
	p['content'] = tweet.text
	p['user'] = tweet.user.screen_name
	p['user_id'] = tweet.user.id_str
	p['time'] = str(tweet.created_at)
	return p


def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
    ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets

# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 80000

tweets = get_tweets(geo = geocode_query,tweet_max = t_max,write = True,out_file = file_name)

tweets.to_csv('data/raw_data.csv', sep=',', encoding='utf-8')
```

### Step 2

Clean up the data so that variations of the same user-provided location name are replaced with a single variation. Once you've cleaned up the locations, create a pie chart of user-provided locations. Your pie chart should strive for legibility! Let the [`matplotlib` documentation](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.pie.html) be your guide!
#### Solution
```Python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# my prefered plot style
plt.style.use('ggplot')

tweets = pd.read_csv('data/raw_data.csv', sep=',')
type(tweets)
# clean duplicated
tweets[tweets.duplicated(subset = 'content', keep = False)].head(2)
tweets.drop_duplicates(subset = 'content', keep = False, inplace = True)
type(tweets)
len(tweets)


# Clean similar Locations
import re
def clear_sim_loc(loc_str,  replace_str , data):
	# Regex char of location string, ignoring cases
	loc_str = re.compile(loc_str, re.IGNORECASE)
	# search and replace based on Regex
	loc = data[data['location'].str.contains(loc_str,na=False)]['location']
	data['location'].replace(loc, replace_str , inplace = True)



loc_list = ['boston','bos','Cambridge','Chelsea','Washington','Massachusetts','USA']
rep_list = ['Boston, MA','Boston, MA','Cambridge, MA','Chelsea, MA','Washinton, DC','Massachusetts, USA','United States']
for i in range(len(loc_list)):
	clear_sim_loc(loc_list[i], rep_list[i] ,tweets)



'Chelsea' in tweets['location'].unique()
len(tweets['location'].unique())


# Locations
loc_tweets = tweets[tweets['location'] != '']
count_tweets = loc_tweets.groupby('location')['id'].count()
df_count_tweets = pd.DataFrame(data = count_tweets)


df_count_tweets = df_count_tweets.reset_index()
df_count_tweets.columns
df_count_tweets.columns = ['locations','count']


# Create a list of colors (from iWantHue)
# colors = ["#697dc6","#5faf4c","#7969de","#b5b246",
#           "#cc54bc","#4bad89","#d84577","#4eacd7",
#           "#cf4e33","#894ea8","#cf8c42","#d58cc9",
#           "#737632","#9f4b75","#c36960"]
# Create a pie chart

def tweet_piechart(data, label):
	plt.figure()
	p1 = plt.pie(data['count'],labels = label,shadow=False)
	plt.axis('equal')
	plt.tight_layout()
	plt.title('Tweets Locations Counts')

	plt.show()

tweet_piechart(data=df_count_tweets, label = df_count_tweets.index.get_values())

df_count_tweets.iloc[258]
# this is messy
import seaborn as sns
sns.set_style('whitegrid')
sns.kdeplot(df_count_tweets['count'], bw=0.5)

# what if we kick out those locations with too few tweets
df_count_tweets_new = df_count_tweets[(df_count_tweets['count'] > 30) & (df_count_tweets['count'] < 10000)]
sns.kdeplot(df_count_tweets_new['count'], bw=0.5)
len(df_count_tweets_new)
tweet_piechart(data=df_count_tweets_new, label = df_count_tweets_new['locations'] )# Create a pie chart

df_count_tweets_new

```


### Step 3
Create a scatterplot showing all of the tweets are that are geolocated (i.e., include a latitude and longitude).
#### Solution
```Python

tweets_geo = tweets[tweets['lon'].notnull() & tweets['lat'].notnull()]
len(tweets_geo)
tweets_geo
tweets_geo['lon'].describe()
tweets_geo['lat'].describe()
# We find that the lat column is not float64 dtype. Change it:
tweets_geo['lat'] = tweets_geo['lat'].astype(np.float64)
tweets_geo['lat'].describe()

def tweet_scatter(data):
	p = plt.figure()
	tweets = plt.scatter(data['lon'].astype(np.float64), data['lat'].astype(np.float64), s = 2, color = 'b',alpha = 0.5)
	Point_x =  [42.359416 for i in range(len(data))]
	Point_y =  [-71.093993 for i in range(len(data))]
	BasePoint = plt.scatter(Point_x, Point_y, color = 'r', s = 15)
	plt.title('Tweets Locations')
	plt.xlabel('longitude')
	plt.ylabel('Latitude')
	plt.axis('equal')
	plt.show()

tweet_scatter(tweets_geo)
```
### Step 4

Pick a search term (e.g., "housing", "climate", "flood") and collect tweets containing it. Use the same lat/lon and search radius for Boston as you used above. Dpending on the search term, you may find that there are relatively few available tweets.
#### Solution
```Python
tweets4 = get_tweets(geo = geocode_query, search_term = 'MIT',tweet_max = t_max,write = True,out_file = 'tweets4.json')

tweets.to_csv('data/raw_data4.csv', sep=',', encoding='utf-8')
```
### Step 5

Clean the search term data as with the previous data.
#### Solution
```Python
tweets4 = pd.read_csv('data/raw_data4.csv', sep=',')
len(tweets4)
# clean duplicated
tweets4[tweets4.duplicated(subset = 'content', keep = False)].head(2)
tweets4.drop_duplicates(subset = 'content', keep = False, inplace = True)
len(tweets4)

# Clean similar Locations
len(tweets4['location'].unique())
loc_list = ['boston','bos','Cambridge','Chelsea','Washington','Massachusetts','USA']
rep_list = ['Boston, MA','Boston, MA','Cambridge, MA','Chelsea, MA','Washinton, DC','Massachusetts, USA','United States']
for i in range(len(loc_list)):
	clear_sim_loc(loc_list[i], rep_list[i] ,tweets4)


tweets4['location'].unique()
'boston' in tweets4['location'].unique()
len(tweets4['location'].unique())
```
### Step 6

Create a scatterplot showing all of the tweets that include your search term that are geolocated (i.e., include a latitude and longitude).
#### Solution
```Python
len(tweets4)
tweets4_geo = tweets4[tweets4['lon'].notnull() & tweets4['lat'].notnull()]
len(tweets4_geo)

tweet_scatter(tweets4_geo)

```
### Step 7

Export your scraped Twitter datasets (one with a search term, one without) to two CSV files. We will be checking this CSV file for duplicates and for consistent location names, so make sure you clean carefully!
#### Solution
```Python

tweets.to_csv('data/without_search_term.csv', sep=',', encoding='utf-8')

tweets4.to_csv('data/with_search_term.csv', sep=',', encoding='utf-8')

```
## Extra Credit Opportunity

Build a scraper that downloads and parses the Wikipedia [List of Countries by Greenhouse Gas Emissions page](https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions) using BeautifulSoup and outputs the table of countries as as a CSV.

#### Solution
```Python




```
