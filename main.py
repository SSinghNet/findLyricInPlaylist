import os
import json
from getPlaylistSongs import getPlaylistSongs
from lyricsgenius import Genius
from dotenv import load_dotenv

load_dotenv()

songs = getPlaylistSongs()
lyrics = []

for s in songs:
    genius = Genius(os.getenv("G_CLIENT_ACCESS_TOKEN"))
    songs = genius.search_songs(s["name"] + " " + s["artist"])

    lyrics.append({"name": s["name"], "artist": s["artist"], "lyrics": genius.lyrics(song_url=songs["hits"][0]["result"]["url"])})

    with open("lyrics.json", "w") as outfile:
        json.dump(lyrics, outfile)