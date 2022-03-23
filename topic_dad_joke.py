# this script fetches 1 dad joke from https://icanhazdadjoke.com API based on an user input
import requests
import json

def fetchJoke(string):

    kval_pairs = {'term': string , 'limit' : 1} 
    api = requests.get('https://icanhazdadjoke.com/search', headers={"Accept":"application/json"} , params=kval_pairs ) # Make request to the api
    content = api.json()                                                                                                # transform JSON into a python object
    
    #print(json.dumps(content, indent=2))                                            # prints the JSON fetched from the API to understand how it is structured
    print('----- Fetching Joke -----' + '\n')
    joke = content['results'][0]['joke']                                             # extract the text of the joke from the dictionaries and list
    return joke                                                                      # return the joke

user_word = input('I want a joke about: ')

print(fetchJoke(user_word))

