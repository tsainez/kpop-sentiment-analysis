import pandas as pd

df = pd.read_csv('../data/data.csv', index_col=0)

# Drop all accidental copies
df = df.drop_duplicates()

# Drop all Tweets with the exact same message...
# These could be retweets, spam, etc...
df = df.drop_duplicates(subset=['text'])

# Next, we only want English and Korean tweets...
langs = ['en', 'ko']
df = df[df['lang'].isin(langs)]

# # Let's see what data we have left...
# print(df.info())
# print(df['lang'].value_counts())

# Some of the data was gathered using methods that have left behind artifacts.
# An example would be some broken link strings (always start with https), and also
# all the retweets. 
patterns = [r'(:?https\w+)', r'(:?RT)( )(\w+)']
for pattern in patterns:
    df['text'] = df['text'].str.replace(pattern, '', regex=True)

# df.to_csv('../data/min.csv')

en = df[df['lang'] == 'en']
ko = df[df['lang'] == 'ko']

en.to_csv('../data/en.csv')
ko.to_csv('../data/ko.csv')