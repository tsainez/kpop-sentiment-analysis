# For nice readability...
import sys

# For saving the response data in CSV format
import csv

# For parsing the dates received from twitter in readable formats
import dateutil.parser

# To add wait time between requests
import time

# Helper functions that help us scrape Tweets.
from helpers import *

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

print("\nEnter interval to wait between requests in seconds: ", end='')
interval = input()

# These values should be "none" for the first runtime.
since_id = 0
next_token = None

total = 0 # Tracks the total amount of Tweets retrieved

while(True):
    try:
        url = create_url(keyword, max_results, since_id, next_token)
        json_response = connect_to_endpoint(url[0], headers, url[1])

        # Open OR create the target CSV file
        path = '../data/data.csv'
        csvFile = open(path, "a", newline="", encoding='utf-8')
        csvWriter = csv.writer(csvFile)

        # Loop through each Tweet
        try:
            for tweet in json_response['data']:
                # Pull relevant data from the Tweet object
                created_at = dateutil.parser.parse(tweet['created_at'])
                id = int(tweet['id'])
                lang = tweet['lang']
                text = tweet['text']

                # Is this the most recent Tweet we've gotten so far?
                if id > since_id:
                    since_id = id

                # Clean up the Tweet text...
                text = clean(text, lang)

                # Assemble all data in a list
                res = [id, text, created_at, lang]

                # Append the result to the CSV file
                csvWriter.writerow(res)

            # When done, close the CSV file
            csvFile.close()
        except KeyError:
            sys.exit("\nNo additional Tweets found! Bye.")

        total += json_response['meta']['result_count']
        print("\n\tRetrieved " +
            str(json_response['meta']['result_count']) + " new Tweets.")
        print("\tTotal is now: " + str(total) + " Tweets.")

        try:
            # We will loop through the Tweets until there is no next_token
            next_token = json_response['meta']['next_token']
        except KeyError:
            # If there is no next_token, wait and then poll again. 
            print("\nNo next token. Waiting " + interval + " seconds for next request...")
            time.sleep(int(interval))
        
    except KeyboardInterrupt:
        sys.exit("\n\n\tTotal Tweets retrieved: {}\n\tExiting...\n".format(total))
