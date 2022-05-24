# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
from genericpath import exists
# For dealing with json responses we receive from the API
import json
# For displaying the data after
import pandas as pd
# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata
# To add wait time between requests
import time


def auth():
    print("\n\tRetrieving BEARER_TOKEN from environment variables...")
    return os.getenv('TOKEN')


def create_headers(bearer_token):
    print("\n\tCreating headers...")
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(query, max_results, since_id):
    print("\n\tCreating request URL...")
    # Change to the endpoint you want to collect data from
    url = "https://api.twitter.com/2/tweets/search/recent"

    # change params based on the endpoint you are using
    params = {'query': query,
              'max_results': max_results,
              'tweet.fields': 'lang,created_at'
              }

    if since_id is not None:
        print("\t\tsince_id provided as '{}'".format(since_id))
        print("\t\tRetrieving only new Tweets!")
        params['since_id'] = since_id
    else:
        print("\t\tsince_id not provided.")

    return (url, params)


def connect_to_endpoint(url, headers, params):
    # params object received from create_url function
    print("\n\tConnecting to endpoint...")
    response = requests.request("GET", url, headers=headers, params=params)
    print("\t\tEndpoint Response Code: " + str(response.status_code))

    if response.status_code != 200:
        print('')  # New line to make it more readable.
        raise Exception(response.status_code, response.text)

    return response.json()


path = 'data/'
print("Enter filename for data: ", end='')
path += input()

if not path.endswith(".csv"):
    path += '.csv'

since_id = None  # For now...

if exists(path):
    # TODO: Update since_id to largest (most recent) in the file...
    exit()

print("Preparing to scrape Tweets...")
bearer_token = auth()
headers = create_headers(bearer_token)

print("\nEnter keyword to search by: ", end='')
keyword = input()

print("\nEnter max number of results: ", end='')
max_results = input()

if int(max_results) < 10:
    print("\n\tWARNING: max_results cannot be lower than default value of 10.")
    max_results = 10

while(True):
    url = create_url(keyword, max_results, since_id)
    json_response = connect_to_endpoint(url[0], headers, url[1])

    # Open OR create the target CSV file
    csvFile = open('data.csv', "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    # Loop through each Tweet
    for tweet in json_response['data']:
        # Pull relevant data from the Tweet object
        created_at = dateutil.parser.parse(tweet['created_at'])
        id = tweet['id']
        lang = tweet['lang']
        text = tweet['text']

        # Assemble all data in a list
        res = [id, text, created_at, lang]

        # Append the result to the CSV file
        csvWriter.writerow(res)

    # When done, close the CSV file
    csvFile.close()

    print("\n\tRetrieved " +
          str(json_response['meta']['result_count']) + " total Tweets.")

    # TODO: Run the script every 5 minutes until KeyboardInterrupt
    print("\nWould you like to continue retrieving Tweets using this keyword? \n\ty/n: ", end='')
    prompt = input()

    if prompt != 'y':
        print("\nEnding program.")
        exit()

    # Else, we only want the most recent Tweets...
    most_recent = max(json_response['data'], key=lambda ev: ev['id'])
    since_id = most_recent['id']
