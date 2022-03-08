import requests
import random

def get_random_gif(API_GIPHY_TOKEN):
    url = f'https://api.giphy.com/v1/gifs/random?api_key={API_GIPHY_TOKEN}&tag=&rating=g'
    return requests.get(url).json()['data'][0]['url']

def get_gifs_url(GIF_NAME, API_GIPHY_TOKEN):
    url = f'https://api.giphy.com/v1/gifs/search?api_key={API_GIPHY_TOKEN}&q={GIF_NAME}&limit=30&offset=0&rating=g&lang=en'
    gifs_url = [requests.get(url).json()['data'][x]['url'] for x in range(len(requests.get(url).json()['data']))]
    choice = gifs_url[random.randint(0,30)]
    return choice


