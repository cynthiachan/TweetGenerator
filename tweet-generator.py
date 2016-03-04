#!/usr/bin/env python
import sys
from TwitterSearch import *

#--------------------------------------------------------------------------------------------------------------
# TweetGenerator - A simple python program which returns a random tweet based on 'keyword' search.
# This program should accept the 'keyword' as a param to your python function.
# Author: Cynthia H. Chan
#--------------------------------------------------------------------------------------------------------------

#prompts user for fileName, keyword
fileName, keyword = raw_input("prompt: ").split(' ')

#randomTweet - returns a json object, or a tweet
def randomTweet(keyword):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([keyword]) #our keyword that we want to look for
        tso.set_include_entities(False) # and don't give us all those entity information

        #-----------------------------------------------------------------
        # We create a TwitterSearch object with our secret tokens.
        # These tokens are needed for user authentication.
        # Credentials generated at: https://apps.twitter.com/app/new
        #-----------------------------------------------------------------

        ts = TwitterSearch(
            consumer_key = "XxXxXxxXXXxxxxXXXxXX",
            consumer_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx",
            access_token = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX",
            access_token_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"
         )
     # counter to keep track of row of json
        counter = 0
      # Iterate through tweets and return a json object, returns first tweet in object
        for tweet in ts.search_tweets_iterable(tso):
            if (counter == 0):
                return tweet
            counter = counter + 1
    except TwitterSearchException as e: # takes care of errors if there are any
        print(e)

# main method - calls randomTweet method and prints out details of tweet
# if file is not entered as the name of the file, prints incorrect file

def main():
    if(fileName == "tweet-generator.py"):
        tweet = randomTweet(keyword)
        print( '@%s: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        print( 'media: %s '% ( tweet['user']['url']) )
    else:
        print("Incorrect file.")

#calls main()
if __name__ == "__main__":main()
