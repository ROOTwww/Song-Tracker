from sys import argv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

song_list = {}
if len(argv) > 1:
    cid = argv[1]
    secret = argv[2]
    username = argv[3]
    try:
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
        playlists = sp.user_playlists(username)
    except Exception as e:
        print(e)
        exit()
else:
    print("usage: tracker.py [client id from api] [client secret key from api] [username from web player]")
    exit()

while playlists:
    for playlist in playlists['items']:
        for track in sp.user_playlist_tracks(username, playlist['uri'])['items']:
            if track["track"]["name"] in song_list:
                print(playlist['name'], track["track"]["album"]["artists"][0]["name"], track["track"]["name"], "PREVIOUS: ", song_list[track["track"]["name"]])
            else:
                song_list[track["track"]["name"]] = playlist['name']
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

