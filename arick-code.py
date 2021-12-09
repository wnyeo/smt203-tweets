import pandas as pd
import snscrape.modules.twitter as sntwitter

keyword= 'plant based meat' 
from_date = '2020-01-01' 
end_date = '2020-12-31' 
max_tweet = 10000
loc = '36.084621, -96.921387, 5000km'


tweets_list = [] 

# Using TwitterSearchScraper to scrape data and append tweets to list 
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:en since:' +  from_date + ' until:' + end_date + ' -filter:links -filter:replies -filter:retweets'.format(loc)).get_items()): 
    tweets_list.append([tweet.date,tweet.id,tweet.username,tweet.content]) 

    if i>max_tweet: 
        break 

# print(tweets_list)
print(len(tweets_list))
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime','Tweet Id','Username', 'Text']) 
tweets_df.to_csv(f'final-covid.csv', index = False)
# pd.set_option('display.max_colwidth', 150) 
