from cmu_graphics import *
from PIL import Image
from ast import literal_eval
import csv

#* CITATION: general button class structure from lecture -> button.py
class Button:
    def __init__(self, x, y, width, height, text, pageIn, pageTo, func):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.pageIn = pageIn
        self.pageTo = pageTo
        self.func = func
    
    def draw(self):
        #* CITATION: got this color from https://cs3-112-f22.academy.cs.cmu.edu/notes/3829
        pistachio = rgb(147, 197, 114)
        drawRect(self.x, self.y, self.width, self.height, fill=pistachio)
        drawLabel(self.text, self.x+(self.width/2), self.y+(self.height/2), 
                  size=25, bold=True)

    def checkForPress(self, app, mX, mY):
        left, top = self.x, self.y
        right, bottom = self.x+self.width, self.y+self.height

        if (app.page == self.pageIn and left <= mX <= right and
            top <= mY <= bottom):
            app.error = False
            app.page = self.pageTo
            if self.func == 'back':
                app.text = ''

class InputBox:
    def __init__(self, x, y, width, height, text, pageTo):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.pageTo = pageTo
    
    def draw(self, app):
        drawRect(self.x, self.y, self.width, self.height, fill=None,
                 border='black', borderWidth=1)
        drawLabel(app.text, self.x+(self.width/2), self.y+(self.height/2))
    
    def enterKey(self, app, key):
        if key == 'enter':
            for user in app.users:
                if self.text == user:
                    app.selectedUser = user
                    #if new selected user -> update all data 
                    resetUser(app)
                    app.page = self.pageTo
                else:
                    app.error = True
        else:
            app.text += key
            self.text = app.text
    
    def deleteKey(self, app, key):
        app.text = app.text[:len(self.text)-1]
        self.text = app.text

class Graph:
    def __init__(self, cx, cy, r, audioFeature, stat):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.audioFeature = audioFeature
        self.stat = stat
    
    def draw(self):
        drawLabel(self.audioFeature, self.cx, self.cy-(self.r*1.5), bold=True)
        drawCircle(self.cx, self.cy, self.r, fill=None, border='black')
        drawCircle(self.cx, self.cy, self.r*self.stat, fill='red')
        drawLabel(f'{int(self.stat*100)}%', self.cx, self.cy+(self.r*1.25))

def onAppStart(app):
    app.width, app.height = 1000, 700

    #user
    app.users = ['kaitlynng', 'yujunwu', 'kendrawong']
    app.selectedUser = 'kaitlynng'

    #selecting zodiac
    app.audioFeatures = getAudioFeatures(app)
    app.averages = averageData(app)
    app.zodiac = getZodiacAnimal(app)
    app.description = getDescription(app)

    #get zodiac songs
    app.trackCovers, app.trackNames, app.trackArtists = getTrackFeatures(app)

    #buttons
    app.page = 0
    app.bWidth, app.bHeight = 200, 50
    app.startButton = Button((app.width/2)-(app.bWidth/2), 
                             (app.height/2)+(app.bHeight*3), app.bWidth, 
                             app.bHeight,'Enter User', 0, 1, 'start')
    app.returnButton1 = Button(50, app.height-(app.bHeight*2), 
                               app.bWidth, app.bHeight, 'Back to Main', 1, 0, 'back')
    app.returnButton2 = Button(50, app.height-(app.bHeight*2), 
                               app.bWidth, app.bHeight, 'Back to Main', 2, 0, 'back')
    app.zodiacSongsButton = Button((app.width/2)-((app.bWidth+40)/2), app.height-(app.bHeight*2),
                                  app.bWidth+40, app.bHeight, 'Your Zodiac Songs', 2, 3, None)
    app.returnButton3 = Button(50, app.height-(app.bHeight*2), 
                               app.bWidth, app.bHeight, 'Back to Zodiac', 3, 2, None)
    #textbox
    app.error = False
    app.text = ''
    app.tWidth, app.tHeight = 200, 25
    app.textBox = InputBox((app.width/2)-(app.bWidth/2), (app.height/2), 
                           app.tWidth, app.tHeight, app.text, 2)

    #images
    #* CITATION: general image import from lecture -> basicPILMethods.py
    app.titleImage = Image.open('titlePage.jpg')
    app.titleWidth, app.titleHeight = app.titleImage.width, app.titleImage.height
    app.titleImage = CMUImage(app.titleImage)

    app.zodiacImage, app.zodiacWidth, app.zodiacHeight = getZodiacImage(app)
    app.zodiacImage = CMUImage(app.zodiacImage)
    
def getZodiacImage(app):
    zodiacs = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig']
    for zodiac in zodiacs:
        if app.zodiac.lower() == zodiac:
            zodiacImage = Image.open(f'{zodiac}.jpg')
            zodiacWidth, zodiacHeight = zodiacImage.width, zodiacImage.height
    return zodiacImage, zodiacWidth, zodiacHeight

#* CITATION: csv file as dict from https://python-adv-web-apps.readthedocs.io/en/latest/csv.html
#get audio feature data from CSV file
def getAudioFeatures(app):
    csvfile = open(f'Spotify Data ({app.selectedUser}).csv', newline='')
    data = csv.DictReader(csvfile)
    return data

def averageData(app):
    acousticness, energy, valence = [], [], []

    for row in app.audioFeatures:
        acousticness.append(float(row['acousticness']))
        energy.append(float(row['energy']))
        valence.append(float(row['valence']))
    
    avgAcousticness = sum(acousticness) / len(acousticness)
    avgEnergy = sum(energy) / len(energy)
    avgValence = sum(valence) / len(valence)

    averages = {'acousticness': avgAcousticness, 
                'energy': avgEnergy,
                'valence': avgValence}
    return averages

def getZodiacAnimal(app):
    zodiac = {'Rat': {'acousticness': 0.3,
                      'energy': 0.5,
                      'valence': 0.4},
              'Ox': {'acousticness': 0.9,
                     'energy': 0.2,
                     'valence': 0.4},
              'Tiger': {'acousticness': 0.1,
                        'energy': 0.8,
                        'valence': 0.7},
              'Rabbit': {'acousticness': 0.8,
                         'energy': 0.3,
                         'valence': 0.8},
              'Dragon': {'acousticness': 0.3,
                         'energy': 0.9,
                         'valence': 0.6},
              'Snake': {'acousticness': 0.7,
                        'energy': 0.3,
                        'valence': 0.2},
              'Horse': {'acousticness': 0.1,
                        'energy': 0.9,
                        'valence': 0.7},
              'Sheep': {'acousticness': 0.7,
                        'energy': 0.4,
                        'valence': 0.6},
              'Monkey': {'acousticness': 0.2,
                         'energy': 0.9,
                         'valence': 0.7},
              'Rooster': {'acousticness': 0.2,
                          'energy': 0.6,
                          'valence': 0.5},
              'Dog': {'acousticness': 0.3,
                      'energy': 0.9,
                      'valence': 0.9},
              'Pig': {'acousticness': 0.2,
                      'energy': 0.7,
                      'valence': 0.4}}

    bestDifference, bestZodiac = None, None
    for animal in zodiac:
        totalDifference = 0

        #calculate average diff across all features betw user and zodiac 
        animalFeatures = zodiac[animal]
        for feature in animalFeatures:
            for myFeature in app.averages:
                if feature != myFeature:
                    continue
                else:
                    difference = abs(animalFeatures[feature] - 
                                     app.averages[myFeature])
                    totalDifference += difference
        avgDifference = totalDifference / len(app.averages)

        #match user to zodiac with smallest diff in features 
        if bestDifference == None or avgDifference <= bestDifference: 
            bestDifference = avgDifference
            bestZodiac = animal
    return bestZodiac 

def getDescription(app):
    if app.zodiac == 'Rat':
        app.description = ["With middling acousticness, energy, and valence",
                           "(how 'positive' or 'negative' your music sounds), you are the rat!",
                           "The rat is incredibly intelligent and quick-witted,",
                           "but private and a little sneaky... You are the hidden ace!"]
                            
    elif app.zodiac == 'Ox':
        app.description = ["With incredibly high acousticness, low energy,", 
                           "and middling valence (how 'positive' or 'negative' your music sounds),",
                           "you are the ox! The ox is hardworking and gentle, but can be a little",
                           "stubborn and lazy."]
    elif app.zodiac == 'Tiger':
        app.description = ["With extremely low acousticness and extremely high energy",
                           "and valence (how 'positive' or 'negative' your music sounds),",
                           "you are the tiger! The tiger is brave and confident (maybe a little too confident).",
                           "Roar your loudest roar proudly!"]
    elif app.zodiac == 'Rabbit':
        app.description = ["With high valence (how 'positive' or 'negative' your music sounds)",
                           "plus high acousticness, and low energy, you are the rabbit!",
                           "Although you are timid, you are kind and sensitive!"]
    elif app.zodiac == 'Dragon':
        app.description = ["With low acousticness, high energy, and neutral valence",
                           "(how 'positive' or 'negative' your music sounds), you are the dragon!",
                           "Although you may be a bit of a perfectionist, people appreciate",
                           "your outspokenness and powerful energy!"]
    elif app.zodiac == 'Snake':
        app.description = ["With strong acousticness and middling energy and valence",
                           "(how 'positive' or 'negative' your music sounds), you are the snake!",
                           "You are clever and alluring, albeit a little stealthy..."]
    elif app.zodiac == 'Horse':
        app.description = ["With extremely low acousticness and high energy and valence",
                           "(how 'positive' or 'negative' your music sounds), you are the horse!",
                           "You can't stay quiet a lot of the times, but you're amusing and enthusiastic!"]
    elif app.zodiac == 'Sheep':
        app.description = ["With high acousticness and middling energy and valence",
                           "(how 'positive' or 'negative' your music sounds), you are the sheep!",
                           "Although a little lazy, you are easygoing and empathetic!"]
    elif app.zodiac == 'Monkey':
        app.description = ["With low acousticness and high energy and valence",
                           "(how 'positive' or 'negative' your music sounds), you are the monkey!",
                           "Although you can be loud and unpredictable, many think you're",
                           "entertaining and intelligent!"]
    elif app.zodiac == 'Rooster':
        app.description = ["With middling energy and valence (how 'positive' or 'negative' your music sounds)",
                           "and low acousticness, you are the rooster. Sometimes you're boastful,",
                           "but you're considered funny and adventurous! Cock-a-doodle-do!"]
    elif app.zodiac == 'Dog':
        app.description = ["With low acousticness and extremely high energy and valence",
                           "(how 'positive' or 'negative' your music sounds), you are the dog!",
                           "You can anxious or timid sometimes, but many consider you loyal and trustworthy!"]
    elif app.zodiac == 'Pig':
        app.description = ["With middling acousticness and valence (how 'positive' or 'negative' your music sounds),",
                           "and somewhat high energy, you are the pig! You might be fearful sometimes, but",
                           "many consider you caring and generous!"]
    return app.description

#get track details data from CSV file
def getTrackFeatures(app):
    csvfile = open(f'Track Data ({app.selectedUser}).csv', newline='')
    data = csv.DictReader(csvfile)

    trackCovers, trackNames, trackArtists = [], [], []
    for row in data:
        album = row['album']
        artist = row['artists']
        #*CITATION: string into dict from https://stackoverflow.com/questions/34246101/how-to-unstring-a-list-tuple-without-eval
        album, artist = literal_eval(album), literal_eval(artist)
        
        trackCovers.append(album['images'][0]['url'])
        trackNames.append(row['name'])
        trackArtists.append(artist[0]['name'])
    return trackCovers, trackNames, trackArtists

def resetUser(app):
    app.audioFeatures = getAudioFeatures(app)
    app.averages = averageData(app)
    app.zodiac = getZodiacAnimal(app)
    app.description = getDescription(app)
    app.zodiacImage, app.zodiacWidth, app.zodiacHeight = getZodiacImage(app)
    app.zodiacImage = CMUImage(app.zodiacImage)
    app.trackCovers, app.trackNames, app.trackArtists = getTrackFeatures(app)

def onMousePress(app, mouseX, mouseY):
    app.startButton.checkForPress(app, mouseX, mouseY)
    app.returnButton1.checkForPress(app, mouseX, mouseY)
    app.returnButton2.checkForPress(app, mouseX, mouseY)
    app.zodiacSongsButton.checkForPress(app, mouseX, mouseY)
    app.returnButton3.checkForPress(app, mouseX, mouseY)

def onKeyPress(app, key):
    if app.page == 1:
        if key == 'backspace':
            app.error = False
            app.textBox.deleteKey(app, key)
        else:
            app.textBox.enterKey(app, key)

def redrawAll(app):
    #homepage
    if app.page == 0:
        newWidth, newHeight = app.titleWidth//2, app.titleHeight//2
        drawImage(app.titleImage, app.width/2, app.height/3, align='center',
                  width=newWidth, height=newHeight)
        app.startButton.draw()
    
    #user login
    if app.page == 1:
        drawLabel('Enter Username', app.width/2, app.height/2-(app.tHeight*2), size=30, bold=True)

        app.textBox.draw(app)
        app.returnButton1.draw()
        
        if app.error: 
            drawLabel('user does not exist', app.width/2, 
                      app.height/2+(app.tHeight+10), fill='red')

    #zodiac info
    if app.page == 2:
        drawLabel(f'You are the {app.zodiac}!', app.width/2, app.height/10, 
                  size=50, bold=True)
        
        newWidth, newHeight = app.zodiacWidth//4, app.zodiacHeight//4
        drawImage(app.zodiacImage, app.width/3, app.height/2.25, align='center',
                  width=newWidth, height=newHeight)
        
        yValue = -10
        for line in app.description:
            yValue += 10
            drawLabel(line, app.width/3, app.height*0.7+yValue)

        yValue = -10
        radius = 40
        for feature in app.averages:
            yValue += 150
            Graph(app.width*0.75, app.height/25+(radius+yValue), radius,
                    feature, app.averages[feature]).draw()
        app.zodiacSongsButton.draw()
        app.returnButton2.draw()

    if app.page == 3:
        #songs 1-5
        xValue = -100
        for i in range(5):
            xValue += 200
            trackCover = app.trackCovers[i]
            trackName = app.trackNames[i]
            trackArtist = app.trackArtists[i]

            #* CITATION: CMU Images from https://cs3-112-f22.academy.cs.cmu.edu/notes/4197
            imageWidth, imageHeight = getImageSize(trackCover)
            drawImage(trackCover, xValue, app.height/8, align='center', width=imageWidth//7, height=imageHeight//7)

            trackNameHeight = app.height/8+(imageHeight//7/1.5)
            drawLabel(f'{trackName} -', xValue, trackNameHeight, align='center')
            drawLabel(trackArtist, xValue, trackNameHeight+15, align='center')

        #songs 6-10
        xValue = -100
        for i in range(5, 10):
            xValue += 200
            trackCover = app.trackCovers[i]
            trackName = app.trackNames[i]
            trackArtist = app.trackArtists[i]

            imageWidth, imageHeight = getImageSize(trackCover)
            drawImage(trackCover, xValue, app.height/8+(1.5*imageHeight//7), align='center', width=imageWidth//7, height=imageHeight//7)

            trackNameHeight = (app.height/8+(1.5*imageHeight//7))+(imageHeight//7/1.5)
            drawLabel(f'{trackName} -', xValue, trackNameHeight, align='center')
            drawLabel(trackArtist, xValue, trackNameHeight+15, align='center')

        #songs 10-15
        xValue = -100
        for i in range(10, 15):
            xValue += 200
            trackCover = app.trackCovers[i]
            trackName = app.trackNames[i]
            trackArtist = app.trackArtists[i]

            imageWidth, imageHeight = getImageSize(trackCover)
            drawImage(trackCover, xValue, app.height/8+(3*imageHeight//7), align='center', width=imageWidth//7, height=imageHeight//7)
            
            trackNameHeight = app.height/8+(3*imageHeight//7)+(imageHeight//7/1.5)
            drawLabel(f'{trackName} -', xValue, trackNameHeight, align='center')
            drawLabel(trackArtist, xValue, trackNameHeight+15, align='center')

        #songs 16-20
        xValue = -100
        for i in range(15, 20):
            xValue += 200
            trackCover = app.trackCovers[i]
            trackName = app.trackNames[i]
            trackArtist = app.trackArtists[i]

            imageWidth, imageHeight = getImageSize(trackCover)
            drawImage(trackCover, xValue, app.height/8+(4.5*imageHeight//7), align='center', width=imageWidth//7, height=imageHeight//7)

            trackNameHeight = app.height/8+(4.5*imageHeight//7)+(imageHeight//7/1.5)
            drawLabel(f'{trackName} -', xValue, trackNameHeight, align='center')
            drawLabel(trackArtist, xValue, trackNameHeight+15, align='center')
        
        app.returnButton3.draw()

runApp()