import pandas as pd
import numpy as np
import re

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

# this is tweet 1529695694868852736
text = "RT allkpop HYBE is not considering replacing or removing Kim Garam from LESSERAFIM httpstcocjAukxvlD"
pattern = r'(:?https\w+)' # find the broken links...

# print(re.findall(pattern, text)) 

df = pd.read_csv('../data/data.csv')
# df.id = df.id.astype(np.int64)
# print(df)
# print(df.loc[df['id'] == 1529695694868852736].text)

# df['text'] = df['text'].str.replace(pattern, '', regex=True)

# print(df.loc[df['id'] == 1529695694868852736].text)
count = 0
for index, row in df.iterrows():
    text = row['text']
    # if re.findall(pattern, text):
    #     count += 1
    print(text)

# print(count)
