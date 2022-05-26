#
# clean.py
#     Scratchwork for figuring out how to clean up the Tweet text...
#

import preprocessor as p
import string
import re

# An example of a real, very messy Tweet (id 1529645159012794368)
text = '''"RT @R1KIC4RT: wts lfb ph #ai_sells

enhypen downsizing sale 🥣
— PRICE ON PICTURE
↳ CAN TINGI, dm for condition
↳ payo / 5 days reservation…"'''

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
text = '''르세라핌 김채원 사쿠라 포카 포토카드 양도해요 

김채원 채원 사쿠라 쿠라 카즈하 홍은채 허윤진 포카 위버스샵 특전 미공포 양도 쇼케이스 럭드 공방 엠투유 파스테 케타포 사웨 photocard https://t.co/OefnJmwsI3'''

print(text)

text = p.clean(text)

print(text)  # Uh oh... It gets rid of all Korean text...
