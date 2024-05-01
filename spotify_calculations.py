from dotenv import load_dotenv
import requests
import json
import os
import sqlite3
import regex
import matplotlib.pyplot as plt



#CALCULATIONS

"""calculate_artist_by_popularity_lastfm takes in the database as an argument, and extracts the last fm artist names and respective play counts using database JOINS, 
it then parses thru the data adding only the artists that have more than 1 track appearing in the data (for data vize purposes) then returns a dictionary where the keys 
represent the artists and the values represent each play count integer from the songs we pulled from that artist. For example: {'The Weeknd': [27869063, 12253723]. . . }"""


def calculate_artist_by_popularity_lastfm(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   out = {}
   cur.execute('SELECT spot_artists.artist_name, lastfm_songs.play_counts FROM lastfm_songs JOIN spot_artists ON lastfm_songs.artist_id = spot_artists.id')
   data = cur.fetchall()
   #print(data)
   for row in data:
      #print(row[0])
      if row[0] not in out:
         in_list = []
         for row_2 in data:
            if row[0] == row_2[0] and row_2[1] != None:
               in_list.append(row_2[1])
         if len(in_list) > 1:
            out[row[0]] = in_list
   print('Dictionary Calculations for Last Fm')
   print(out)
   print('\n\n')
   return out

"""calculate_artist_by_popularity_spotify takes in the database as an argument, and extracts the spotify artist names and respective play counts using database JOINS, 
it then parses thru the data adding only the artists that have more than 1 track appearing in the data (for data vize purposes), then returns a dictionary where the keys 
represent the artists and the values represent each popularity rating () from the songs we pulled from that artist. For example:  'The Weeknd': [90, 83]"""


def calculate_artist_by_popularity_spotify(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   out = {}
   cur.execute('SELECT spot_artists.artist_name, spotify_songs.song_popularity FROM spotify_songs JOIN spot_artists ON spotify_songs.artist_id = spot_artists.id')
   data = cur.fetchall()
   #print(data)
   for row in data:
      #print(row[0])
      if row[0] not in out:
         in_list = []
         for row_2 in data:
            if row[0] == row_2[0] and row_2[1] != None:
               in_list.append(row_2[1])
         if len(in_list) > 1:
            out[row[0]] = in_list

   print('Dictionary Calculations for Spotify')
   print(out)
   print('\n\n')
   return out

"""calculate_artist_by_popularity_soundcloud takes in the database as an argument, and extracts the soundcloud artist names and respective play counts using database JOINS, 
it then parses thru the data adding only the artists that have more than 1 track appearing in the data (for data vize purposes), then returns a dictionary where the keys 
represent the artists and the values represent each play count integer from the songs we pulled from that artist. For example: {}'The Weeknd': [988, 98] """


def calculate_artist_by_popularity_soundcloud(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   out = {}
   cur.execute('SELECT spot_artists.artist_name, soundcloud_songs.play_counts FROM soundcloud_songs JOIN spot_artists ON soundcloud_songs.artist_id = spot_artists.id')
   data = cur.fetchall()
   #print(data)
   for row in data:
      #print(row[0])
      if row[0] not in out:
         in_list = []
         for row_2 in data:
            if row[0] == row_2[0] and row_2[1] != None:
               in_list.append(row_2[1])
         if len(in_list) > 1:
            out[row[0]] = in_list

   print('Dictionary Calculations for SoundCloud')
   print(out)
   print('\n\n')
   return out


#VISUALIZATION


"""The functions (create_lastfm_viz_artist, create_spotify_viz_artist, create_soundcloud_viz_artist) each take in a dictionary representing the returned output of the calculation functons above, and they
 create the matplotlib vizualistations for the respective streaming services. We made Boxplots for each of them to make a comparison for how frequent each of the artist's selected songs are on different streaming
 service platforms; noted for play counts for last fm and soundcloud, and popularity metrics for Spotify."""


def create_lastfm_viz_artist(dictionary):
    artists = sorted(dictionary.keys(), key = lambda i: dictionary[i])
    play_counts = sorted(dictionary.values(), key =lambda i: i)
  
    plt.figure(figsize=(12,8))
    plt.subplots_adjust(bottom=0.15)
    plt.boxplot(play_counts, labels=artists, vert=False)
    plt.xlabel('Play Counts')
    plt.ylabel('Last FM Artists')
    plt.title('Box and Whisker Plot of Last FM Artists vs Play Counts (in tens of millions)')
    plt.tight_layout()
    plt.show()


def create_spotify_viz_artist(dictionary):
    artists = sorted(dictionary.keys(), key = lambda i: dictionary[i])
    play_counts = sorted(dictionary.values(), key =lambda i: i)

    plt.figure(figsize=(12,8))
    plt.subplots_adjust(bottom=0.15)
    plt.boxplot(play_counts, labels=artists, vert=False)
    plt.xlabel('Popularity Counts')
    plt.ylabel('Spotify Artists')
    plt.title('Box and Whisker Plot of Spotify Artists vs Popularity Counts')
    plt.tight_layout()
    plt.show()


def create_soundcloud_viz_artist(dictionary):
    artists = sorted(dictionary.keys(), key = lambda i: dictionary[i])
    play_counts = sorted(dictionary.values(), key =lambda i: i)

    plt.figure(figsize=(12,8))
    plt.subplots_adjust(bottom=0.15)
    plt.boxplot(play_counts, labels=artists, vert=False)
    plt.xlabel('Play Counts')
    plt.ylabel('Soundcloud Artists')
    plt.title('Box and Whisker Plot of Soundcloud Artists vs Play Counts (in tens of millions)')
    plt.tight_layout()
    plt.show()
   




   
   

def main():
   database = input("Enter the name of the database here: ")
   print('\n\n')
   #'API_Audio_FusionDB.db'

   data_lastfm = calculate_artist_by_popularity_lastfm(database)
   data_lastfm
   create_lastfm_viz_artist(data_lastfm)

   data_spotify = calculate_artist_by_popularity_spotify(database)
   create_spotify_viz_artist(data_spotify)
   data_spotify

   soundcloud_data = calculate_artist_by_popularity_soundcloud(database)
   soundcloud_data
   create_soundcloud_viz_artist(soundcloud_data)

if __name__ == "__main__":
    main()