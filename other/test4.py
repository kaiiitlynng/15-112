import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from cmu_graphics import *

#export SPOTIPY_CLIENT_ID='9d3d158cd29f446b877597f60e60f981'
#export SPOTIPY_CLIENT_SECRET='859926ee51194570a3631958e59d43ef'
#export SPOTIPY_REDIRECT_URI='https://localhost8888/callback'

# urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# artist = sp.artist(urn)
# print(artist)

# user = sp.user('plamere')
# print(user)

id = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'
track = sp.track(id)
audio = sp.audio_features(id)
# print(audio)
print(audio[0]['acousticness'])
result = []
for feature in audio:
    for feature:
        if not key == 'acousticness':
            del feature[key]
print(audio)
        