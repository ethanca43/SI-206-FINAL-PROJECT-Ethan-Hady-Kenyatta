from bs4 import BeautifulSoup
import os
import re
import sqlite3


"""Scrap takes in a filename of an html file which contains the soundcloud webpages for all of 
the songs and then uses beautiful soup to fetch the play counts of each song/track. It then returns
 the id of the song pulled from the data base and an integer representing the play count number. 
 For example, if you inputed ‘38_Greedy_ArianaGrande.html’ as the argument, the it would return (38, [290212])"""


def scrap(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)
    with open(full_path, mode = 'r', encoding ="utf-8-sig") as openfile:
         #print(openfile)
         data = openfile.read()
         nl = []
         #print(data)

         soup = BeautifulSoup(data, 'html.parser')
         get_span= soup.find_all("span", class_="sc-ministats")
         #print(get_span[0].text)
         reg = re.findall('\d+,?\d+,?\d+', get_span[0].text)
         #print(reg[0])

         out = int(reg[0].replace(',',''))
         #print(filename.split('/')[-1].split('_')[0])
         #print(filename)
         id = filename.split('/')[-1].split('_')[0]
         return id, out
    

"""Add_info_to_database takes in the info, a tuple (the one generated in Scrap) and the database 
and creates the soundcloud_songs table. To the table it inserts the song name, artist name, and play counts
for the song (Selecting the info based of the ID number)"""

def add_info_to_database(info, database):
    #connecting to DB
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + database)
    cur = conn.cursor()

    cur.execute(f'SELECT artist_id FROM spotify_songs WHERE id = "{info[0]}"')
    artist = cur.fetchone()[0]
    print(artist)

    cur.execute(f'SELECT name FROM spotify_songs WHERE id = "{info[0]}"')
    song = cur.fetchone()[0]
    print(song)

    cur.execute('CREATE TABLE IF NOT EXISTS soundcloud_songs (id INTEGER, name TEXT UNIQUE, artist_id INTEGER, play_counts INTEGER)')
    cur.execute('INSERT OR IGNORE INTO soundcloud_songs (id,name,artist_id,play_counts) VALUES(?,?,?,?)', (info[0], song, artist, info[1]))                                                                                                    
    conn.commit()
    conn.close()





def main():
  
  database = input("Enter the name of the database here: ")
  #database = 'API_Audio_FusionDB.db'
  full_song_lst = []
  for filename in os.listdir('soundcloud_htmlsongs'):
    if '.html' in filename:
       info = scrap(f'soundcloud_htmlsongs/{filename}')
       full_song_lst.append(info)
 

    #database loads
  print('Loading the first 25 rows of data into db!')
  print('\n\n')
  accum_1 = 1
  data_load_1 = full_song_lst[:25]
  for song_info in data_load_1:
    add_info_to_database(song_info,database)
    accum_1 += 1
      
  print('Loading the second batch of 25 data rows into db!')
  accum_2 = 26
  data_load_2 = full_song_lst[25:50]
  for song_info in data_load_2:
    add_info_to_database(song_info,database)
    accum_2 += 1    
      

  print('Loading the third batch of 25 data rows into db!')
  accum_3 = 51
  data_load_3 = full_song_lst[50:75]
  for song_info in data_load_3:
    add_info_to_database(song_info,database)
    accum_3 += 1   
      
  print('Loading the fourth batch of 25 data rows into db!')
  accum_4 = 76
  data_load_4 = full_song_lst[75: ]
  for song_info in data_load_4:
    add_info_to_database(song_info,database)
    accum_4 += 1   





if __name__ == "__main__":
    main()




