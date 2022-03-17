import re

def get_artist_id(spotify, name):
    results = spotify.search(q='artist:' + name, type='artist')
    print(results)
    return results['artists']['items'][0]['id']

def get_top_n_tracks(spotify, artist, n = 10):
    artist_id = get_artist_id(spotify, artist)
    results = spotify.artist_top_tracks(artist_id)
    tracks = "**" + artist + "**'s top " + str(n) + " tracks:\n"
    for i in range(n):
        tracks = tracks + str(i+1) + " : " + results['tracks'][i]['name'] + "   " + results['tracks'][i]['external_urls']['spotify'] + "\n"
    return tracks

def get_last_n_albums(spotify, artist, n = 10):
    artist_id = get_artist_id(spotify, artist)
    results = spotify.artist_albums(artist_id, album_type='album', limit = 50)
    albums = "**" + artist + "**'s albums:\n"
    if n > int(results['total']): n = int(results['total'])
    for i in range(n):
        albums = albums + results['items'][i]['name'] + "   " + results['items'][i]['external_urls']['spotify'] + "\n"
    return albums

def get_n_related_artists(spotify, artist, n = 10):
    artist_id = get_artist_id(spotify, artist)
    results = spotify.artist_related_artists(artist_id)
    similar_artist = "**" + artist + "**'s similar artists:\n"
    if n > 20: n = 20
    for i in range(n):
        similar_artist = similar_artist + results['artists'][i]['name'] + "   " + results['artists'][i]['external_urls']['spotify'] + "\n"
    return similar_artist

def get_user_id(spotify, username):
    user = spotify.user(username)
    print(user)
    #photo = user['images'][0]['url']
    return user#['uri']

def get_artist(spotify, track):
    results = spotify.search(q= track, type='track')
    return results['tracks']['items'][0]['artists'][0]['name'] + " sang " + track

#def get_response(spotify, user_input):
#    if((re.search("artist|singer|group|boysband|band|girlsband", user_input)) and (re.search("related to|similar to|like", user_input))):
#        pattern = re.compile(r"related to |similar to |like ")
#        splitted=pattern.split(user_input)
#        artist = splitted[-1][:-1]
#        return (get_n_related_artists(spotify, artist))
#    elif(re.search("artist|singer|group|boysband|band|girlsband", user_input)):
#        pattern = re.compile(r"sang |sing ")
#        splitted=pattern.split(user_input)
#        track = splitted[-1][:-1]
#        return (get_artist(track, USER_SPOTIFY_TOKEN))
#    elif(re.search("(W|w)ho", user_input)):
#        pattern = re.compile(r"sang |sing ")
#        splitted=pattern.split(user_input)
#        track = splitted[-1][:-1]
#        print("\n Track:", track)
#        return (get_artist(track, USER_SPOTIFY_TOKEN))
#    elif(re.search('best musics|best music|top|top musics|top tracks', user_input)):
#        pattern = re.compile(r'of |from |by ')
#        splitted=pattern.split(user_input)
#        artist = splitted[-1][:-1]
#        return (get_top_n_tracks(spotify, artist))
#    else:
#        return ("I **didn't** get it. Could you rephrase please ?")