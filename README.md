## zhuan-112
## CMU 15-112 Spring 23 Term Project: Zhuan

### Project Description

Zhuan is an application built with Python 3 that takes a user’s Spotify data from the last 6 months (by connecting to the user’s Spotify account) and tells the user what their Zodiac animal is. Additionally, they will provided information about their songs’ audio features (acousticness, energy, and valence) and what their 20 most played songs actually are (their “Zodiac” songs). 

### How to Run Zhuan

To run the actual application:
1. open “ZHUAN.py”
2. press command/control + b

The actual application has preexisting users as shown in the titles of the provided CSV files (“kaitlynng”, “yujunwu”, and “kendrawong”) that you may use. 

If you would like to see your specific Spotify data:
1. email kaitlynng790@gmail.com
2. provide your first and last name
3. provide the email you used to make your Spotify account
   
Once you are confirmed to use the app (you get an email reply back):
1. open “spotipyData.py”
2. assuming spotipy is imported, copy and paste lines 6-8 one by one into your terminal
3. update the “username” in line 31 with your preferred username
4. run the application by typing into terminal: “python3 spotipyData.py”
5. follow the instructions given by the terminal
6. a Spotify Data CSV file should be created
7. open “ZHUAN.py”
8. append your username to app.users in line 87
9. open “getTrackInfo.py”
10. assuming spotipy is imported, copy and paste lines 5-7 one by one into your terminal
11. update the “username” in lines 11 and 31 with your preferred username
12. run the application by typing into terminal: “python3 getTrackInfo.py”
13. follow the instructions (if any) given by the terminal
14. a Track Data CSV file should be created

The reason you cannot directly authenticate yourself with Spotify is due to the fact Zhuan is in development mode: only users the developers has specifically screened can use the application. In the future, Zhuan will be moved to extended quota mode, where any user can use the application without any restriction. 

### Libraries to Install

To gather the data necessary to view your specific Spotify data, you will need to install “Spotipy”.

Spotipy documentation can be found here: https://spotipy.readthedocs.io/en/2.22.1/

To install Spotipy:
1. type into terminal “python3 -m pip” to ensure that “Pip” is recognized
2. type “python3 -m pip install spotipy”
3. if there is an spotipy update available type into terminal the command provided to update 

You will also need to install CMU Graphics.

Instructions to download are found here: https://cs3-112-f22.academy.cs.cmu.edu/desktop
