import requests

API_KEY = "89fe8b6fdb992ba0d56e0abd370674e3a11aa16d"
POST_URL = "http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities"


def make_request(text):
    outputMode = "json"
    sentiment = 1
    post_data = {'apikey': API_KEY, 'text': text, 'outputMode': outputMode,
                 'sentiment': sentiment}
    ret_data = requests.post(url=POST_URL, data=post_data)
    return ret_data.json()


make_request("I have long fantasized about Apple burning down the\
              Internet of ads.")
