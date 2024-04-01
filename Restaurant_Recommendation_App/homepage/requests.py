# Implement here the Requests
import requests
from django.conf import settings

#API KEY
API_KEY = '57743afd58msh45c17bff9dca66cp1df63djsn2738777c500b'
API_HOST = settings.API_HOST


# Currency settings
def currency():
    url = "https://worldwide-restaurants.p.rapidapi.com/currencies"

    headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": API_HOST
    }

    response = requests.get(url, headers=headers)

    print(response.json())

# Language support
def language():
    url = "https://worldwide-restaurants.p.rapidapi.com/languages"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.get(url, headers=headers)

    print(response.json())

# typeAhead
def typeAhead(restaurant_name):
    url = "https://worldwide-restaurants.p.rapidapi.com/typeahead"

    payload = {
        "q": restaurant_name,
        "language": "en_US"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()

# Search for existing Restaurants
def search(location_id):
    url = "https://worldwide-restaurants.p.rapidapi.com/search"
    payload = {
        "language": "en_US",
        "location_id": location_id,
        "currency": "PHP",
        "offset": "0"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()

# Restaurant Details
def details():
    url = "https://worldwide-restaurants.p.rapidapi.com/detail"

    payload = {
        "currency": "USD",
        "language": "en_US",
        "location_id": "15333482"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())

# Restaurant photos
def photos():
    url = "https://worldwide-restaurants.p.rapidapi.com/photos"

    payload = {
        "location_id": "15333482",
        "language": "en_US",
        "currency": "USD",
        "offset": "0"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())

# Restaurant Reviews
def reviews():
    url = "https://worldwide-restaurants.p.rapidapi.com/reviews"

    payload = {
        "location_id": "15333482",
        "language": "en_US",
        "currency": "USD",
        "offset": "0"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())