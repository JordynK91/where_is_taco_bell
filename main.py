from art import tprint
from api import SearchAPI
from dotenv import load_dotenv
import os

# if you don't have .env file you can put Yelp API key here
token = ''
BEARER_TOKEN = os.getenv('BEARER_TOKEN', token)

def hola_mundo():
    tprint('Where is Taco Bell')
    print('Hello! Welcome to Where Is Taco Bell, the Taco Bell locator service')
    valid_selection = False
    while not valid_selection:
        selection_raw = input('Type CITY to search by city. Type ZIPCODE to search by zipode. Type EXIT to exit the program\n')
        selection = selection_raw.lower()
        if selection == 'city':
            valid_selection = True
            city_search()
        elif selection == 'zipcode':
            valid_selection = True
            zip_search()
        elif selection == 'exit':
            valid_selection = True
            print('Goodbye!')
            break
        else:
           print("I'm sorry, I don't recognize that input. Try again?\n")
    print("Thanks for using Where is Taco Bell!")
    return


def zip_search():
    zip = input('Please enter the zip code you would like to search.\n')
    while len(zip) != 5:
        zip = input('Sorry, that is not a valid zip code. Please try again.\n')
    do_search(zip)

def city_search():
    city = input('Please enter the city you would like to search.\n')
    # assuming there are no cities in the world with one letter names
    while len(city) < 2:
          city = input('Sorry, that is not a valid city name. Please try again.\n')
    do_search(city)


def do_search(location):
    if not token:
        print('Fatal Error: We are missing the Yelp API Key. Goodbye.')
        return
    status, tbell_list = SearchAPI(token).search_by_location(location)
    if status == 1:
      print('Uh oh! We had a problem searching for Taco Bells.')
      return
    taco_bell_len = len(tbell_list)
    if taco_bell_len == 0:
        print("We're sorry. We found no open Taco Bells in your area.")
        return
    print(f'We found {taco_bell_len} open Taco Bells!')
    for idx, x in enumerate(tbell_list):
        tbell_number = (idx+1)
        address = x.get('address')
        phone = x.get('phone')
        print(f"Taco Bell #{tbell_number}:")
        print(f"Address: {address}")
        print(f"Phone: {phone}")


hola_mundo()



