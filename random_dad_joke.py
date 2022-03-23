# this script fetches a random dad joke from https://icanhazdadjoke.com API
import requests
import json

def fetchJoke():

    api = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"}) # Make request to the api
    content = api.json()                                                                    # transform JSON into a python object

    #print(json.dumps(content, indent=2))               # prints the JSON fetched from the API to understand how it is structured
    print('----- Fetching Joke -----' + '\n')

    return content['joke']                                                                  # return the joke

print(fetchJoke())