import pandas as pd

df = pd.read_csv('../data/data.csv', index_col=0)
# data.set_index('id')

# Drop all accidental copies
df = df.drop_duplicates()

# Drop all Tweets with the exact same message...
# These could be retweets, spam, etc...
df = df.drop_duplicates(subset=['text'])

# Next, we only want English and Korean tweets...
langs = ['en', 'ko']
df = df[df['lang'].isin(langs)]

# Let's see what data we have left...
print(df.info())
print(df['lang'].value_counts())

df.to_csv('../data/min.csv')