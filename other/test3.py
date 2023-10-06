import spotipy
from spotipy.oauth2 import SpotifyOAuth
from cmu_graphics import *

#export SPOTIPY_CLIENT_ID='9d3d158cd29f446b877597f60e60f981'
#export SPOTIPY_CLIENT_SECRET='859926ee51194570a3631958e59d43ef'
#export SPOTIPY_REDIRECT_URI='https://localhost8888/callback'

def onAppStart(app):
    app.width, app.height = 500, 500
    app.scope = "user-top-read" #user-library-read
    app.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=app.scope))
    app.results = app.sp.current_user_top_tracks(time_range='medium_term')
    app.images = []
    for i, item in enumerate(app.results['items']):
        app.images.append(item['album']['images'][0]['url'])

def redrawAll(app):
    imageWidth, imageHeight = getImageSize(app.images[0])
    drawImage(app.images[0], 200, 200, align='center',
                  width=imageWidth//2, height=imageHeight//2)

def main():
    runApp()

if __name__ == '__main__':
    main()