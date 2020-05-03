import twitter
import tweepy
from textblob import TextBlob
import matplotlib as mpl

class SentimentAnalysis:

    def __init__(self, search, count, result_type, until, lang):
        self.search = search
        self.count = count
        self.result_type = result_type
        self.until = until
        self.lang = lang

    def call_api(self):
        #Standard Twitter API Keys
        consumer_key = "sTHGIyqNhYPyDTxr4UlBf77Vk"
        consumer_key_secret = "cN1NQTLA69Y8khRSX90FKCYJLcv6SdRCwDrN0SAynMeEAvSfMF"
        access_token = "1236369835384168448-nRxodOp86kDjkU29Vlh9rj3ESMKE3j"
        access_token_secret = "ATbfpnRpxjYLQWclOqsRfHPIXzYRjs0ZPKwRcmcQp3Juk"

        #Tweepy library connects to Twitter API authentification
        auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        #API Call
        public_tweets = api.search(q = self.search, count = self.count, result_type = self.result_type, until = self.until, lang = self.lang)

        #Values for analysis
        positive_count = 0
        negative_count = 0

        #Textblob NLP Analysis
        for tweet in public_tweets:
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            print(analysis.sentiment)
            if analysis.sentiment[0]>0:
                print('Positive')
                positive_count += 1
            else:
                print('Negative')
                negative_count += 1
            print("")

        #Print statements to console
        total_count = positive_count + negative_count
        if positive_count > negative_count:
            print("Sentiment towards %s is positive: %d positive tweets, %d negative tweets" % (self.search, positive_count, negative_count))
        elif positive_count < negative_count:
            print("Sentiment towards %s is negative: %d positive tweets, %d negative tweets" % (self.search, positive_count, negative_count))
        else:
            print("Sentiment towards %s is indifferent" % (self.search))

if __name__ == "__main__":

    search = input('Search term: ')
    count = 100
    result_type = 'recent'
    until = '2020-03-13'
    lang = 'en'

    model = SentimentAnalysis(search, count, result_type, until, lang)
    model.call_api()
