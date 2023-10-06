import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

#* copy paste in terminal to connect spotify api 
# export SPOTIPY_CLIENT_ID='9d3d158cd29f446b877597f60e60f981'
# export SPOTIPY_CLIENT_SECRET='859926ee51194570a3631958e59d43ef'
# export SPOTIPY_REDIRECT_URI='https://localhost8888/callback'

#* CITATION: extracting user data from spotify from https://spotipy.readthedocs.io/en/2.22.1/
scope = "user-top-read"
auth = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
client = spotipy.Spotify(client_credentials_manager=
                              SpotifyClientCredentials())
topTracks = auth.current_user_top_tracks(time_range='medium_term')

trackIDs = []
for i, item in enumerate(topTracks['items']):
    trackIDs.append(item['id'])

audioFeatures = []
for id in trackIDs:
    audioFeatures.append(client.audio_features(id).pop())

#* CITATION: creating csv file from https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
fieldNames = ['danceability', 'energy', 'key', 'loudness', 
               'mode', 'speechiness', 'acousticness', 'instrumentalness',
               'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 
               'track_href', 'analysis_url', 'duration_ms', 'time_signature']

with open('Spotify Data (username).csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(audioFeatures)
