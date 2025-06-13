# K-pop Sentiment Analysis

[Final Report](https://drive.google.com/file/d/10eTQegxI1bIGuIC1wzGb-VBPBKkuU6JL/view?usp=sharing) 

Prepared by [Anthony Sainez](mailto:asainez@ucmerced.edu) and [Jingyi Jennie Wu](mailto:jingyi_wu@umail.ucsb.edu) in collaboration with Barun ICT Research Center \[[en](https://www.barunict.org)\] \[[kr](http://barunict.kr)\] at Yonsei University in Seoul, South Korea.

This repository contains data collected during May 2022 for use in sentiment analysis of K-pop related Tweets.

## Context

The data seeks to explore the controversy surrounding [Hybe entertainment](https://hybecorp.com/eng/main)'s new girl group [Le Sserafim](https://le-sserafim.com)— a member of which (Kim Garam, 김가람) is alleged to have been a bully during her schooling.

Hybe is an internationally successful and recongizable entertainment company, known mainly for their most influential boy band [BTS](https://en.wikipedia.org/wiki/BTS), which is the best-selling artist in South Korean history among other accolades.

## Data

### Data description

- `data.csv`
  - Contains the complete and raw dataset, including all language results polled from Twitter during our search periods.
  - Search queries included: `[Hybe, Le Sserafim, 르세라핌, Garam, 김가람, #garamout]`
- `data_clean.csv` contains the cleaned dataset, which represents a 31.75% decrease in size.

  - Data clean up involved:
    - Removing duplicate rows.
    - Removing text that is not in English or Korean.
    - Removing suspected advertisements or spam.
  - Korean text was not cleaned up in the same manner as English text.

- `data_ko.csv` and `data_en.csv` contain only the Korean and English results respectively.
  - `data_ko.csv` also contains a column (`en_text`) corresponding to the translated text (from Korean to English), using Google Cloud Translate API.

### Data samples

For `data_en.csv`:
|id |text |created_at |lang|
|-------------------|---------------------------------------------------------------------------------------------------------------------|-------------------------|----|
|1529696231739383808|fuck you hybe |2022-05-26 05:29:36+00:00|en |
|1529717794786271232| Listen if you support Kim Garam but believe that Soojin deserved to be kicked out of GIDLE do not talk to me Soojin…|2022-05-26 06:55:17+00:00|en |
|1529720463953387522| anyway no center ever could outdo garam |2022-05-26 07:05:54+00:00|en |
|1529720293987700736| garam’s face is top tier kimgaram 김가람 르세라핌 |2022-05-26 07:05:13+00:00|en |

For `data_ko.csv`:
|id |text |en_text |created_at |lang|
|-------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----|
|1529696402145955840|야가람아아이돌하고싶었으면김가람탈퇴해학폭을하지를말았어야지garamout민폐끼치지말고제발나가주라쏘스뮤직해명해너없으면모두가행복해탈퇴해 |Yagaram, if you wanted to be an idol, you should have left Kim Garam and didn’t have to be abusive. |2022-05-26 05:30:17+00:00|ko |
|1529695383567613952|르세라핌넘무잘해요 |Le Seraphim is so good |2022-05-26 05:26:14+00:00|ko |
|1529727257207783424|너네좆됨김가람쏘스뮤직병신들아ㅋㅋ |Fuck you, Kim Garam Source Music bastards hahaha |2022-05-26 07:32:53+00:00|ko |
|1529727063254761472|누가둘사이원래친구였고틀어진게궁금하대미성년자둘사이자질구레한관계변화일대기를왜대체인터넷에공지로뿌리냐고회사가김가람이학교폭력으로무려보호처분호를받은그상세내용이궁금하…|I wonder who was originally friends and what went wrong between the two of them. I&#39;m curious as to the details of how the company, Kim Ga-ram, received a protective measure due to school violence...|2022-05-26 07:32:07+00:00|ko |

### Notable complications

- A lot of this data is seriously dirty.
  - Some of the text has been cleaned in various different ways as we learned different processes that worked (and did not work) for preprocessing the data.
    - For instance, there is still some Korean in the English dataset (possibly hashtags) that are an artifact from a previous method of text mining and preprocessing.
  - Additionally, there are still some irrelevant pieces of text in the data, such as advertisements and giveaways that we did not manage to catch on our first pass.
- This data was collected through a polling process, whereby we repeatedly scraped Twitter for new data. We chose this approach because we were not able to access any data that is older than 7 days or historical data. Our application for Twitter's Academic Research API v2 was denied, and we were not allowed to reapply.
  - The data collection process would be incredibly simplified if another team manages to gain access to the aforementioned API, and would likely result in better analysis. Nevertheless, the process and code to create such a dataset is provided with as much documentation as possible.

## Reproducibility

To run and generate the dataset yourself:

1. Clone the repository::

   ```
   git clone https://github.com/tsainez/kpop-sentiment-analysis
   cd kpop-sentiment-analysis
   ```

2. Create and activate a virtual environment::

   ```
   python3 -m venv venv
   . venv/bin/activate
   ```

3. Install Python dependencies::

   ```
   pip3 install -r requirements.txt
   ```

4. Run the files in the `scripts` directory in order.

### TODO:

- Adjust scripts to not require human intervention to run.
- Create a Makefile for ease of reproducibility.
