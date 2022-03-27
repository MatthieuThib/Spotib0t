<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Logos/Spotib0t_light.png?raw=true" width="200" align="right"/>

## Click here to [add **Spotib0t** to your server](https://discord.com/api/oauth2/authorize?client_id=950439738106597467&permissions=8&scope=bot)

## :musical_note: What is **Spotib0t** ?
Spotibot is a bot for discord. It is build in python using [discord.py](https://github.com/Rapptz/discord.py) library. <br>
The idea is to interact with Spotib0t to get musical data about a song or an artist.

<hr>

## :speech_balloon: Chatbot
Using regular expressions, Spotib0t is able to detect an artist name or a song title in some patterns. Then, it fetchs data from the [spotify API](https://developer.spotify.com/documentation/web-api/) by calling [spotipy](https://spotipy.readthedocs.io/en/2.19.0) library functions.
Spotib0t can get you:
- The singer of a track
- The lasts albums of an artist
- The top tracks of an artist
- The related artists of an artist
- Information about a spotify user
## :bulb: Recommendation system

As mentionned before, The spotify API provides an endpoint to get the related artists of an artist, but it is based on the uses of spotify user so it is not very personnal.
That's why we build a specific recommendation system for Spotib0t.
Using a spotify dataset about music features, we were able to set up a kmeans clustering algorithm to find similar tracks.

## :mag_right: Commands
The prefix of Spotib0t is ```$``` but you can change it in *main.py*.
+ ```$join``` -> Spotib0t logs in
+ ```$quit``` -> Spotib0t logs out
+ ```$gif``` -> Spotib0t gets you a gif from [*giphy*](https://giphy.com) (gif_name)
+ ```$del``` -> Spotib0t deletes the last messages (number_of_messages)

## :pushpin: Examples

<details>
<summary>Get Spotify user informations</summary>
You can get the followers of a spotify user just by tiping the username. The user can be an artist as well as a regular spotify user.
<p align="left">
<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Examples/EminemInformation.png" width="600" />
</p>
<br>
</details>

<details>
<summary>Get singer of a track</summary>
You can get the singer of a track just by asking to Spotib0t:
<p align="left">
<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Examples/KidCudiSangCudiZone.png" width="600" />
</p>  
<br>
</details>

<details>
<summary>Get an artist's top tracks</summary>
You can get the current top tracks of an artist by asking to Spotib0t:
<p align="left">
<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Examples/KidCudiTopTrack.png" width="600" />
</p>  
<br>
</details>

<details>
<summary>Get an artist's last albums</summary>
Spotib0t can get you the last albums of an artist:
<p align="left">
<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Examples/DaftPunkAlbums.png" width="600" />
</p>  
<br>
</details>


<details>
<summary>Get an artist recommendation</summary>
Using the spotify API related artists endpoint, Spotib0t can get you similar artists:
<p align="left">
<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Examples/DrakeSimilarArtists.png" width="600" />
</p>  
<br>
</details>

<details>
<summary>Get track recommendations</summary>
With a kmeans clustering on a spotify dataset, Spotib0t can get you similar tracks:
<p align="left">
<img src="https://github.com/MatthieuThib/Spotib0t/blob/main/Examples/CudiZoneSimilarTracks.png" width="600" />
</p>  
<br>
</details>

## :clap: Contributors
+ TEMPO Chloé - [@chlotmpo](https://github.com/chlotmpo)
+ YUNG Sébastien - [@SebYg00](https://github.com/SebYg00)
+ THIBAUT Matthieu - [@MatthieuThib](https://github.com/MatthieuThib)
