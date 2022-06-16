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
import emoji
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


def create_url(query, max_results, since_id, next_token):
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

    if next_token is not None:
        print("\t\tNext token is {}".format(next_token))
        params['next_token'] = next_token
    else:
        if since_id != 0:
            print("\t\tRetrieving Tweets newer than {}!".format(since_id))
            params['since_id'] = since_id
        else:
            print("\t\tsince_id not provided.")

    return (url, params)


def connect_to_endpoint(url, headers, params):
    '''Sends a HTTP GET request to the specified endpoint.'''

    # 'params' object should be received from create_url() function
    print("\n\tConnecting to endpoint...")
    response = requests.request("GET", url, headers=headers, params=params)
    print("\t\tEndpoint Response Code: " + str(response.status_code))

    if response.status_code != 200:
        print('')  # New line to make it more readable.
        raise Exception(response.status_code, response.text)

    return response.json()


def clean(text, lang):
    '''Cleans up Tweets before putting them into a CSV to ensure no errors
    in reading back. Note that we do not tokenize, stem or lemmatize.'''

    # We use a different process for Korean and English text. 
    if lang == 'en':
        # For English, we can use the already built Tweet preprocessing library...
        return p.clean(text)
    elif lang == 'ko':
        # Korean text must be preprocessed manually, as the library we use above would 
        # actually get rid of all the Korean text.

        # Remove links from the text.
        text = re.sub(r'http\S+', '', text)

        # Get rid of special symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        text = "".join([char for char in text if char not in string.punctuation])
        text = re.sub('[0-9]+', '', text)

        # Replace new lines with spaces
        text = text.replace('\n', ' ')

        # Remove emojis
        text = emoji.replace_emoji(text, replace='')

        return text
