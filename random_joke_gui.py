import requests
import json
from tkinter import *            

# this script fetches a random dad joke from https://icanhazdadjoke.com API

# fetch joke and diplay it on the GUI
def fetchJoke():

    api = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"}) # Make request to the api
    content = api.json()                                                                    # transform JSON into a python object
    #print(json.dumps(content, indent=2))                                                   # prints the JSON fetched from the API to understand how it is structured
    
    joke = content['joke']                                                                  # extracts the text from the JSON 

    loading = Label(root, text= '----- Fetching Joke -----' + '\n' , pady = 10 )            # label prints on the UI
    loading.grid(row = 3 , column=1)                                                        # the grid positions the elements    
    
    #access the input window where the text will be displayed
    e.delete(0 ,END)                                                                        # delete the previous text before inserting the new one   
    e.insert(0, joke)                                                                       # insert new text 
    
    #return joke         

def main():
    # create the root widget, always the first thing of the GUI program
    global root                                                                             # global so it can be accessed by the fetchJoke function
    root = Tk()
    root.title('Joke Fetcher')

    # label widget to display text
    title = Label(root , text = 'Welcome to fetch a random joke!' + '\n' + 'Click the button to get a joke!' )  
    space = Label(root, text = '  ')                                                        # just leaves a space for a nicer look

    # input field to show result
    global e                                                                                 # global so it can be accessed by the fetchJoke function
    e = Entry(root, width = 100, borderwidth = 5, justify='center' )

    #grid system
    title.grid(row = 0, column = 1)
    space.grid(row = 1, column = 1)
    e.grid(row = 4 , column=0 , columnspan = 3, padx = 10, pady = 10)

    # buttons
    jokeButton = Button(root, text = 'Joke me', command = fetchJoke , padx = 25 , pady = 25 , bg = 'orange' , fg = 'black') 
    jokeButton.grid(row = 2 , column = 1)

    # run mainloop() to be able to run the interface
    root.mainloop() 

main()
