import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests

myd = {}
cid = ''#Client ID from API
secret = ''#Client Secret from API
username = ''#Username to get playlists from
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        #print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        for track in sp.user_playlist_tracks(username, playlist['uri'])['items']:
            #print(playlist['name'], track["track"]["album"]["artists"][0]["name"], track["track"]["name"])
            if track["track"]["name"] in myd:
                print(playlist['name'], track["track"]["album"]["artists"][0]["name"], track["track"]["name"], "PREVIOUS: ", myd[track["track"]["name"]])
            else:
                myd[track["track"]["name"]] = playlist['name']
                print(myd[track["track"]["name"]])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

