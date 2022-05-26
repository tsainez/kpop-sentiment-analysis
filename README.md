# K-pop Sentiment Analysis

Prepared by [Anthony Sainez](mailto:asainez@ucmerced.edu) and [Jingyi Jennie Wu](mailto:jingyi_wu@umail.ucsb.edu) in collaboration with Barun ICT Research Center \[[en](https://www.barunict.org)\] \[[kr](http://barunict.kr)\] at Yonsei University in Seoul, South Korea.

This repository contains data collected during May 2022 for use in sentiment analysis of K-pop related Tweets.

## Context

The data seeks to explore the controversy surrounding [Hybe entertainment](https://hybecorp.com/eng/main)'s new girl group [Le Sserafim](https://le-sserafim.com)— a member of which is alleged to have been a bully during her schooling.

Hybe is an internationally successful and recongizable entertainment company, known mainly for their most influential boy band [BTS](https://en.wikipedia.org/wiki/BTS), which is the best-selling artist in South Korean history among other accolades.

# Notable complications

- This data was collected through a polling process, whereby we repeatedly scraped Twitter for new data. We chose this approach because we were not able to access any data that is older than 7 days or historical data. Our application for Twitter's Academic Research API v2 was denied, and we were not allowed to reapply.

# Reproducibility

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

## TODO:

- Adjust scripts to not require human intervention to run.
- Create a Makefile for ease of reproducibility.
