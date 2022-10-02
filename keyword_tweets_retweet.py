import os
from twitter_bot_class import Twitter_Bot
"""
Retweet the tweets depending on the keywords you entered
"""
if __name__ == "__main__":
    try:
        EMAIL = input("Provide your Phone, email or username: ")
        PASSWORD = input("Provide your password: ")
        tbot = Twitter_Bot(EMAIL,PASSWORD)
        tbot.login()
        kw=input('Enter keyword')#Enter keyword to search tweets for retweeting
        tbot.search(kw)
        tbot.retweet(10)
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)
