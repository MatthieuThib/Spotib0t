import re
import pandas as pd

from recommendation_system import recommend_tracks

def get_artist_id(spotify, name):
    """ Returns the spotify id of an artist """
    results = spotify.search(q='artist:' + name, type='artist')
    if len(results['artists']['items'])>0:
        return results['artists']['items'][0]['id']
    return ""

def get_track_id(spotify, track):
    """ Returns the spotify id of a track """
    results = spotify.search(q= track, type='track')
    return results['tracks']['items'][0]['id']

def get_user_id(spotify, username):
    """ Returns the user id of a username """
    user = spotify.user(username)
    return user['uri']

def get_track_info(spotify, track):
    results = spotify.search(q = track.replace("-", ""), type='track')
    if 'tracks' in results.keys():
        return results['tracks']['items'][0]['name'] + " - " + results['tracks']['items'][0]['album']['artists'][0]['name'] + "   " + results['tracks']['items'][0]['external_urls']['spotify']
    return ""
    
def get_top_n_tracks(spotify, artist, n = 10):
    """ Returns the n most popular tracks of an artist """
    artist_id = get_artist_id(spotify, artist)
    results = spotify.artist_top_tracks(artist_id)
    if 'tracks' in results.keys():
        tracks = "**" + artist.capitalize() + "**'s top " + str(n) + " tracks:\n"
        for i in range(n):
            tracks = tracks + str(i+1) + " : " + results['tracks'][i]['name'] + "   " + results['tracks'][i]['external_urls']['spotify'] + "\n"
        return tracks
    return ""

def get_last_n_albums(spotify, artist, n = 10):
    """ Returns the n most recent albums of an artist """
    artist_id = get_artist_id(spotify, artist)
    results = spotify.artist_albums(artist_id, album_type='album', limit = 50)
    albums = "**" + artist.capitalize() + "**'s albums:\n"
    if n > int(results['total']): n = int(results['total'])
    for i in range(n):
        albums = albums + results['items'][i]['name'] + "   " + results['items'][i]['external_urls']['spotify'] + "\n"
    return albums

def get_n_related_artists(spotify, artist, n = 10):
    """ Returns the n most related artists of an artist """
    artist_id = get_artist_id(spotify, artist)
    results = spotify.artist_related_artists(artist_id)
    similar_artist = "**" + artist.capitalize() + "**'s similar artists:\n"
    if n > 20: n = 20
    for i in range(n):
        similar_artist = similar_artist + results['artists'][i]['name'] + "   " + results['artists'][i]['external_urls']['spotify'] + "\n"
    return similar_artist

def get_user_info(spotify, username):
    """ Returns the user link and number of followers of a username """
    user = spotify.user(username)
    if 'followers' in user.keys():
        userinfo = f"**{username.capitalize()}**'s information on spotify:\n Folowers: {user['followers']['total']} \n Link: {user['external_urls']['spotify']}"
        return userinfo
        
    else:
        return "**" + username + "** not found on spotify"

def get_artist(spotify, track):
    """ Returns the artist of a track """
    results = spotify.search(q= track, type='track')
    return "**" + results['tracks']['items'][0]['artists'][0]['name'] + "** sang " + track + "\n" + results['tracks']['items'][0]['external_urls']['spotify']

def get_track_name_and_year(spotify, track):
    """ Returns the name and year of a track (dict)"""
    results = spotify.search(q = track, type='track')
    return {"name": track.lower().capitalize(), 'year': int(results['tracks']['items'][0]['album']['release_date'][:4])}

def get_audio_features(spotify, track):
    """ Returns the audio features of a track """
    track_id = get_track_id(spotify, track)
    results = spotify.search(q= track, type='track', limit = 1)
    audio_features = spotify.audio_features(track_id)[0]
    track_data = {}
    track_data['name'] = [track]
    track_data['year'] = [int(results['tracks']['items'][0]['album']['release_date'][:4])]
    track_data['explicit'] = [1 if(results['tracks']['items'][0]['explicit']) else 0]
    track_data['duration_ms'] = [results['tracks']['items'][0]['duration_ms']]
    track_data['popularity'] = [results['tracks']['items'][0]['popularity']]
    
    for key, value in audio_features.items():
        track_data[key] = value

    return track_data

def get_song_vectors(spotify, song_list):
    """ Returns the song vectors for a list of songs """
    number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']
    song_vectors = []
    
    for song in song_list:
        song_data = pd.DataFrame(get_audio_features(spotify, song))
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)  
        
    return song_vectors


def get_response(spotify, user_input):
    if user_input[-1] != "?": user_input += "?"
    
    user_input_lower = user_input.lower()
    if((re.search("artist|singer|group|boysband|band|girlsband", user_input_lower)) and (re.search("related to|similar to|like", user_input_lower))):
        pattern = re.compile(r"related to |similar to |like ")
        splitted=pattern.split(user_input)
        artist = splitted[-1][:-1]
        return (get_n_related_artists(spotify, artist))
    
    elif(re.search("artist|singer|group|boysband|band|girlsband", user_input_lower)):
        pattern = re.compile(r"sang |sing |of")
        splitted=pattern.split(user_input)
        track = splitted[-1][:-1]
        return (get_artist(spotify, track))
    
    elif(re.search("(W|w)ho", user_input)):
        pattern = re.compile(r"sang |sing ")
        splitted=pattern.split(user_input)
        track = splitted[-1][:-1]
        return (get_artist(spotify, track))
    
    elif(re.search('best musics|best music|top|top musics|top tracks', user_input_lower)):
        pattern = re.compile(r'of |from |by ')
        splitted=pattern.split(user_input)
        artist = splitted[-1][:-1]
        return (get_top_n_tracks(spotify, artist))
    
    elif(re.search('last albums|last album', user_input_lower)):
        pattern = re.compile(r'of |from |by ')
        splitted=pattern.split(user_input)
        artist = splitted[-1][:-1]
        return (get_last_n_albums(spotify, artist))
    
    elif((re.search("music|track|song|musics|tracks|songs", user_input_lower)) and (re.search("similar to |like", user_input_lower))):
        pattern = re.compile(r"similar to |like ")
        splitted=pattern.split(user_input)
        track = splitted[-1][:-1]
        song_vectors = get_song_vectors(spotify, [track])
        
        reco = "**" + track.capitalize() + "**'s similar tracks:\n"
        tracksss = recommend_tracks(song_vectors)["name"]
        for recommended_track in tracksss:
            print(recommended_track)
            reco += get_track_info(spotify, recommended_track) + "\n"
        return reco
    
    elif(re.search("(G|g)ive me information about|(T|t)ell me about", user_input)):
        pattern = re.compile(r"about ")
        splitted=pattern.split(user_input)
        user = splitted[-1][:-1]
        return get_user_info(spotify, user.replace(" ", ""))
        
    else:
        print("I **didn't** get it. Could you rephrase please ?")