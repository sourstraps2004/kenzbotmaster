import tweepy
import sys
import os import environ
import spotipy
import spotipy.util as util

scope = 'user-read-currently-playing'
username = 'supalups'
PORT_NUMBER = 8888
SPOTIPY_CLIENT_ID = '2b5a2c9b01e4426196eeae9d07b352f7'
SPOTIPY_CLIENT_SECRET = '9caece9efd8f40848d318886a1d018f5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

token = util.prompt_for_user_token(username, scope, '2b5a2c9b01e4426196eeae9d07b352f7', '9caece9efd8f40848d318886a1d018f5', 'http://localhost:8888/callback/')

CONSUMER_KEY = environ['L0viSyy7gDWP0kEVeUtNUpDm6']
CONSUMER_SECRET = environ['gikgZo9fwIovRYL0D2KWqOhN6omW8eEm7Go89cV4mWD5zCyMcR']
ACCESS_TOKEN = environ['1378616618759098368-bP2pcOlX1rIbpnTNFRr22VrIB9extz']
ACCESS_TOKEN_SECRET = environ['k1JA4bIZsJopxiYfsrFQFqXXJmvXLOGSs7Tuz26I0svP8']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

token = util.prompt_for_user_token(username, scope)
                        
spotify = spotipy.Spotify(auth=token)

while True:
    try:
        current_track = spotify.current_user_playing_track()
        current_track_id = current_track['item']['id']

        if current_track_id is not None:
    

            api.update_status("jelly music" + ":" + '\n' + current_track['item']['artists'][0]['name'] + " - " +
                                                                    current_track['item']['name'] + '\n' + str(
                                                                    current_track['item']['external_urls']['spotify']))
            break
        else:
            continue
    except spotipy.client.SpotifyException:
        token = util.prompt_for_user_token(username, scope)

        spotify = spotipy.Spotify(auth=token)
    except (tweepy.TweepError, TypeError) as e:
        pass

while True:
    try:
       new_track = spotify.current_user_playing_track()
       new_track_id = new_track['item']['id']

       if current_track_id is not None and new_track_id != current_track_id:

                                                                                     
           api.update_status("jelly music" + ":" + '\n' + new_track['item']['artists'][0]['name'] + " - " +
                                                  new_track['item']['name'] + '\n' + str(
                                                  new_track['item']['external_urls']['spotify']))
           current_track_id = new_track_id
       else:
           continue
    except spotipy.client.SpotifyException:
         token = util.prompt_for_user_token(username, scope)
         
         spotify = spotipy.Spotify(auth=token)
    except (tweepy.TweepError, TypeError)as e:
         pass                                                                         
