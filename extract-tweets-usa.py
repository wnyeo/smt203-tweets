import pandas as pd
import snscrape.modules.twitter as sntwitter

def slice_date(date):
    return date[:4]

def convert_pdt_tostr(dt):
    return dt.strftime('%Y-%m-%d')

list_keyword = ['plant based meat', 'plant based food', 'impossible food', 'impossible meat', 'beyond meat', 'alternative protein']



loc = '36.084621, -96.921387, 5000km'

for keyword in list_keyword:
    loc = '36.084621, -96.921387, 5000km'
    df = pd.DataFrame(sntwitter.TwitterSearchScraper(
        '{} geocode:"{}"'.format(keyword, loc)).get_items())[['date','content']]
    df.date = df.date.apply(convert_pdt_tostr)
    df.date = df.date.apply(slice_date)
    print(len(df))
    before_df = df[df['date']<= '2019']
    after_df = df[df['date'] > '2019']
    num_b4 = len(before_df)
    num_after = len(after_df)

    before_df.to_csv(f'{keyword}-b4-covid.csv', index = False)
    after_df.to_csv(f'{keyword}-covid.csv', index = False)

    print(f'{keyword} success, before covid: {num_b4}, after covid: {num_after}')





