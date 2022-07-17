import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

def getPlaylistSongs():
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("SP_CLIENT_ID"), client_secret=os.getenv("SP_CLIENT_SECRET"))
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.playlist_items("6zDXvoJU7vLxcu7DtabLsK")["items"]

    songs = []
    for i in results:
        songs.append({"name": i["track"]["name"], "artist": i["track"]["artists"][0]["name"]})

    return songs