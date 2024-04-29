from dotenv import load_dotenv
import requests
import json
import os
import sqlite3
import regex

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
def calculate_genre_frequency(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   out = {}
   cur.execute('SELECT spotify_genres.genre_name FROM spotify_songs JOIN spotify_genres ON spotify_songs.genre_id = spotify_genres.id')
   data = cur.fetchall()
   #print(data)
   general_genres = ['N/A', 'pop', 'funk', 'r&b', 'hip hop', 'rock', 'indie', 'alt', 'other' ]
   for row in data:
      if row[0] not in out:
         out[row[0]] = 1
      else:
        out[row[0]] += 1
   print(out)
   return out

#take dictionary from above function and sorts into general genres
def sort_out_genres(dictionary):
   
   new_d = {'N/A': 39, 'pop':12, 'funk': 3, 'r&b':10, 'hip hop': 4, 'indie': 4, 'rock':2,'alt': 3,'afrofuturism': 2, 'other': 21}
   nl = ['N/A', 'pop', 'funk', 'r&b', 'hip hop', 'indie', 'rock', 'alt', 'afrofuturism', 'other']
  
   out = {'N/A': [a, b ,c]}


   for genre in nl:
      count = 0
      for k, v in dictionary.items():
         if genre in k:
            count += 1


      
      
      
      


   

   
   



def main():
   database = 'API_Audio_FusionDB.db'
   #calculate_explicitnesss(database)
   calculate_genre_frequency(database)

if __name__ == "__main__":
    main()