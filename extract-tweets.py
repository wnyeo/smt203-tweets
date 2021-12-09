import pandas as pd
import snscrape.modules.twitter as sntwitter
import os

def slice_date(date):
    return date[:4]

def convert_pdt_tostr(dt):
    return dt.strftime('%Y-%m-%d')

list_keyword = ['plant based meat', 'plant based food', 'impossible food', 'impossible meat', 'beyond meat', 'alternative protein']
keyword = 'alternative protein'

metadata = {}


with open('us_states.csv', 'r') as f:
    f.readline()
    for line in f:
        line = line.rstrip()
        state, us, lat, long, km, blank = line.split(',')
        state = state[1:]
        # # print(state)
        # # print(lat)
        # # print(long)
        # # print(km)
        loc = f'{lat}, {long}, {km}km'
        try:
            df = pd.DataFrame(sntwitter.TwitterSearchScraper(
                '{} geocode:"{}"'.format(keyword, loc)).get_items())[['date','content']]
            df.date = df.date.apply(convert_pdt_tostr)
            df.date = df.date.apply(slice_date)

            before_df = df[df['date']<= '2019']
            after_df = df[df['date'] > '2019']
            num_b4 = len(before_df)
            num_after = len(after_df)

            os.makedirs(f'{keyword}-data-b4-covid', exist_ok=True)
            os.makedirs(f'{keyword}-data-covid', exist_ok=True)

            before_df.to_csv(f'{keyword}-data-b4-covid/{state}.csv', index = False)
            after_df.to_csv(f'{keyword}-data-covid/{state}.csv', index = False)

            print(f'{state} success, before covid: {num_b4}, after covid: {num_after}')
            metadata[state] = {'before': num_b4, 'after': num_after}
        except:
            print(f'{state} error')
            metadata[state] = {'before': 0, 'after': 0}


with open(f'{keyword}-metadata.csv', 'w') as f:
    f.write('state,before-covid,after-covid\n')
    for key, item in metadata.items():
        to_write = key + ',' + str(item['before']) + ',' + str(item['after']) +'\n'
        f.write(to_write)

