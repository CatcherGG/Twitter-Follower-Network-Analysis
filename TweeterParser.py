import tweepy
import time
import os
consumer_key = '-'
consumer_secret = '-'
access_token = '-'
access_secret = '-'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

if api.verify_credentials:
    print('We successfully logged in')

file = open('C:\DS\CatcherGG.txt', 'w+')
for page in tweepy.Cursor(api.followers, screen_name="CatcherGG").pages():
    time.sleep(60)
    followers = []
    followers.extend(page)
    for follower in followers:
        if not(os.path.exists('C:\DS\\' + follower.screen_name + '.txt')):
            follower_file = open('C:\DS\\' + follower.screen_name + '.txt', 'w+')
            file.write(follower.screen_name)
            file.write("\n")
            try:
                for follower_page in tweepy.Cursor(api.followers, screen_name=follower.screen_name).pages(10):
                    time.sleep(60)
                    followers_of_follower = []
                    followers_of_follower.extend(page)
                    for follower_of_follower in followers_of_follower:
                        follower_file.write(follower_of_follower.screen_name)
                        follower_file.write("\n")
                follower_file.close()
            except tweepy.TweepError:
                time.sleep(60)
                print("Unable to scrap: "+follower.screen_name+" it has protected tweets.")
        else:
            print("Skipping: "+follower.screen_name+" already scrapped it.")
file.close()
