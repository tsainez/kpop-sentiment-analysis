#
# helpers.py
#     This file contains helper functions that assist in the Tweet scraping process.
#

# For accessing system environment variables.
import os

# For sending HTTP GET requests to a desired endpoint.
import requests

# For text cleanup (removal of punctuation)
import preprocessor as p
import string
import re


def auth():
    '''Pulls the TOKEN (bearer token) from your system environment variables.'''

    print("\n\tRetrieving TOKEN from environment variables...")

    token = os.getenv('TOKEN')

    if token is not None:
        return token
    else:
        print("\nNo BEARER_TOKEN found! Quitting...")
        exit()


def create_headers(bearer_token):
    '''Creates the headers for when you send the HTTP request to Twitter.'''

    print("\n\tCreating headers...")
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(query, max_results, since_id):
    '''Creates the URL endpoint to send an HTTP request (GET) to.
    Changes depending on the query (what keyword to search for),
    the max number of results (between 10 and 100), and what the last
    Tweet ID was— searching only for Tweets more recent than that.'''

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
    '''Sends a HTTP GET request to the specified endpoint.'''

    # params object received from create_url function
    print("\n\tConnecting to endpoint...")
    response = requests.request("GET", url, headers=headers, params=params)
    print("\t\tEndpoint Response Code: " + str(response.status_code))

    if response.status_code != 200:
        print('')  # New line to make it more readable.
        raise Exception(response.status_code, response.text)

    return response.json()


def clean(text):
    '''Cleans up Tweets before putting them into a CSV to ensure no errors
    in reading back. Note that we do not tokenize, stem or lemmatize.'''

    text = p.clean(text)  # Takes care of newlines and other tricky stuff...

    # Now get rid of special symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)

    return text
