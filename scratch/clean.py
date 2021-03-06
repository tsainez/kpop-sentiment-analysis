#
# clean.py
#     Scratchwork for figuring out how to clean up the Tweet text...
#

import preprocessor as p
import string
import re

# An example of a real, very messy Tweet (id 1529645159012794368)
text = '''"RT @R1KIC4RT: wts lfb ph #ai_sells

enhypen downsizing sale ๐ฅฃ
โ PRICE ON PICTURE
โณ CAN TINGI, dm for condition
โณ payo / 5 days reservationโฆ"'''

print(text)

text = p.clean(text)

print(text)

# text = text.strip()

# print(text)

# Should remove !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
text = "".join([char for char in text if char not in string.punctuation])
text = re.sub('[0-9]+', '', text)

print(text)  # Finally gets what we want...

# Real Korean tweet, id 1529649623303847937
text = '''๋ฅด์ธ๋ผํ ๊น์ฑ์ ์ฌ์ฟ ๋ผ ํฌ์นด ํฌํ ์นด๋ ์๋ํด์ 

๊น์ฑ์ ์ฑ์ ์ฌ์ฟ ๋ผ ์ฟ ๋ผ ์นด์ฆํ ํ์์ฑ ํ์ค์ง ํฌ์นด ์๋ฒ์ค์ต ํน์  ๋ฏธ๊ณตํฌ ์๋ ์ผ์ผ์ด์ค ๋ญ๋ ๊ณต๋ฐฉ ์ ํฌ์  ํ์คํ ์ผํํฌ ์ฌ์จ photocard https://t.co/OefnJmwsI3'''

print(text)

text = p.clean(text)

print(text)  # Uh oh... It gets rid of all Korean text...
