import requests

def get_artist_id(artist, API_SPOTIFY_TOKEN):
    API_URL = f'https://api.spotify.com/v1/search?q={artist}&type=artist'
    API_URL = API_URL.replace(' ', '%20')
    response = requests.get(
            API_URL,
            headers={
                    "Authorization": f"{API_SPOTIFY_TOKEN} "
            }
    )
    print(response.json())
    #return json_resp['artist']['items'][0]['id']

def get_top_track(artist, API_SPOTIFY_TOKEN):
    aid = get_artist_id(artist, API_SPOTIFY_TOKEN)
    API_URL = f'https://api.spotify.com/v1/artists/{aid}/top-tracks?market=US'
    
    response = requests.get(
            API_URL,
            headers={
                    "Authorization": f"{API_SPOTIFY_TOKEN} "
            }
    )
    
    json_resp = response.json()
    #print(json_resp['tracks'][0]['name'])
    for i in range(len(json_resp['tracks'])):
        print(i+1, " : ", json_resp['tracks'][i]['name'])
        
        
def get_artist(track, API_SPOTIFY_TOKEN):
    API_URL = f'https://api.spotify.com/v1/search?q={track}&type=track&market=US'
    API_URL = API_URL.replace(' ', '%20')

    response = requests.get(
            API_URL,
            headers={
                    "Authorization": f"{API_SPOTIFY_TOKEN} "
            }
    )
    
    json_resp = response.json()
    for i in range(len(json_resp['tracks']['items'])):
        print(json_resp['tracks']['items'][i]['artists'][0]['name'])
