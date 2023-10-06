import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#* copy paste in terminal to connect spotify api 
# export SPOTIPY_CLIENT_ID='9d3d158cd29f446b877597f60e60f981'
# export SPOTIPY_CLIENT_SECRET='859926ee51194570a3631958e59d43ef'

#* CITATION: csv file as dict from https://python-adv-web-apps.readthedocs.io/en/latest/csv.html
ids = []
csvfile = open(f'Spotify Data (username).csv', newline='')
data = csv.DictReader(csvfile)

for row in data:
    ids.append(row['id'])

#* CITATION: extracting track data from spotify from https://spotipy.readthedocs.io/en/2.22.1/
client = spotipy.Spotify(client_credentials_manager=
                              SpotifyClientCredentials())
trackInfo = []
for id in ids:
    track = client.track(id)
    trackInfo.append(track)

# #* CITATION: creating csv file from https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
fieldNames = ['album', 'artists', 'available_markets', 'disc_number',
              'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href',
              'id', 'is_playable', 'linked_from', 'restrictions', 'name', 'popularity',
              'preview_url', 'track_number', 'type', 'uri', 'is_local']

with open('Track Data (username).csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(trackInfo)



