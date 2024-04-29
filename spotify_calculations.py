from dotenv import load_dotenv
import requests
import json
import os
import sqlite3
import regex
import matplotlib.pyplot as plt

#take in database, and loop thru it to determine the counts for the number of explicit songs


#cur.execute(f'SELECT food_types.food_type FROM restaurants JOIN food_types ON restaurants.food_type_id = food_types.id WHERE restaurants.id = {i}')
        #food_type = cur.fetchone()
def calculate_explicitnesss(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   cur.execute('SELECT explicit.explicitness, FROM spotify_songs JOIN explicit ON spotify_songs.explicit_id = explicit.id')
   all_explic_data = cur.fetchall()
   explicit_count = 0
   non_explicit_count = 0
   #print(all_explic_data)
   for row in all_explic_data:
      if row[0] == 'No':
         non_explicit_count+=1
      else:
         explicit_count += 1
   print(f'The number of explicit songs are: {explicit_count}')
   print(f'The number of non explicit songs are {non_explicit_count}')
   return explicit_count, non_explicit_count

#return a dictionary for genre and their counts

def calculate_genres_by_popularity_spotify(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   out = {}
   cur.execute('SELECT spotify_genres.genre_name, spotify_songs.song_popularity FROM spotify_songs JOIN spotify_genres ON spotify_songs.genre_id = spotify_genres.id')
   data = cur.fetchall()
   #print(data)
   #general_genres = ['N/A', 'pop', 'funk', 'r&b', 'hip hop', 'rock', 'indie', 'alt', 'other' ]
   for row in data:
      #print(row[0])
      if row[0] not in out:
         in_list = []
         for row_2 in data:
            if row[0] == row_2[0]:
               in_list.append(row_2[1])
         out[row[0]] = in_list
   #print(out)
   return out



def calculate_genre_by_popularity_lastfm(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   out = {}
   cur.execute('SELECT lastfm_genre_tags.genre_tag, lastfm_songs.play_counts FROM lastfm_songs JOIN lastfm_genre_tags ON lastfm_songs.genretag_id = lastfm_genre_tags.id')
   data = cur.fetchall()
   #print(data)
   #general_genres = ['N/A', 'pop', 'funk', 'r&b', 'hip hop', 'rock', 'indie', 'alt', 'other' ]
   for row in data:
      #print(row[0])
      if row[0] not in out:
         in_list = []
         for row_2 in data:
            if row[0] == row_2[0] and row_2[1] != None:
               in_list.append(row_2[1])
         out[row[0]] = in_list
   print(out)
   return out


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
   print(out)
   return out


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
   return out








#sort_out_keys = sorted(out.keys(), key=lambda i: out[i])


def create_lastfm_viz_genre(dictionary):
    
    #Extracting genre tags and play counts
    genre_tags = sorted(dictionary.keys(), key = lambda i: len(dictionary.keys()[i]))
    play_counts = list(dictionary.values())
    # Create the box plot

    plt.figure(figsize=(12,8))
    plt.subplots_adjust(bottom=0.15)
    plt.boxplot(play_counts, labels=genre_tags, vert=False)
    plt.xlabel('Play Counts')
    plt.ylabel('Genre Tags')
    plt.title('Box and Whisker Plot of Music Genre Tags vs. Play Counts')
    plt.tight_layout()
    plt.show()


def create_lastfm_viz_artist(dictionary):
    
    #Extracting genre tags and play counts
    artists = sorted(dictionary.keys(), key = lambda i: dictionary[i])
    play_counts = sorted(dictionary.values(), key =lambda i: i)
    # Create the box plot

    plt.figure(figsize=(12,8))
    plt.subplots_adjust(bottom=0.15)
    plt.boxplot(play_counts, labels=artists, vert=False)
    plt.xlabel('Play Counts')
    plt.ylabel('Last FM Artists')
    plt.title('Box and Whisker Plot of Last FM Artists vs Play Counts (by tens of millions)')
    plt.tight_layout()
    plt.show()


def create_spotify_viz_artist(dictionary):
    
    #Extracting genre tags and play counts
    artists = sorted(dictionary.keys(), key = lambda i: dictionary[i])
    play_counts = sorted(dictionary.values(), key =lambda i: i)
    # Create the box plot

    plt.figure(figsize=(12,8))
    plt.subplots_adjust(bottom=0.15)
    plt.boxplot(play_counts, labels=artists, vert=False)
    plt.xlabel('Popularity Counts')
    plt.ylabel('Spotify Artists')
    plt.title('Box and Whisker Plot of Spotify Artists vs Popularity Counts')
    plt.tight_layout()
    plt.show()
   


      


   

   
   



def main():
   database = 'API_Audio_FusionDB.db'
   #calculate_explicitnesss(database)
   #calculate_genres_by_popularity_spotify(database)
   # freq_d = calculate_genre_by_popularity_lastfm(database)
   # create_lastfm_viz_genre(freq_d)

   data_lastfm = calculate_artist_by_popularity_lastfm(database)
   data_lastfm
   create_lastfm_viz_artist(data_lastfm)

   data_spotify = calculate_artist_by_popularity_spotify(database)
   create_spotify_viz_artist(data_spotify)

if __name__ == "__main__":
    main()