import requests
import tweepy
import time

headers = {

    'X-CMC_PRO_API_KEY': "e64c7798-d127-495c-934d-cf7a7bd01e9e",
    'Accepts': 'application/json'

}

params = {
    "start": "1",
    "limit": "5",
    "convert":"GBP"
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

jsondata = requests.get(url,params=params,headers=headers).json()

print(jsondata)

cryptos = jsondata["data"]


def tweetOut():
    print("Tweeting Out")
    for x in cryptos:
        api.update_status (x["name"], x["quote"]["GBP"]["price"])
    time.sleep(1)
    print("Tweeted.")

tweetOut()