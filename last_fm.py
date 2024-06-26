from dotenv import load_dotenv
import requests
import json
import os
import sqlite3





"""Get_lastfm_API_Key takes in the filename of a file representing the .txt file which contians our granted API Key for Last FM. It returns the stirng contents of the file."""


def get_lastfm_API_KEY(filename):
  base_path = os.path.abspath(os.path.dirname(__file__))
  full_path = os.path.join(base_path, filename)
  with open(full_path, 'r') as f:
     API_KEY = f.read()
  return API_KEY



"""Get_track_info takes in the API_key, the requested song_name, aned requested artist_name, 
and returns a tuple containing the requested song, artist, the genre (the first genre tag listed in the json repsonse), playcount (how many times 
the song/track has been played) and listener_count (how many users listen to the track on Last FM). The request similarly uses a series of required 
headers and params, in the form of a payload dictionary"""


def get_track_info(API_KEY,song_name, artist_name):
  headers = {
     'user-agent': 'ethanca43'
     }
  payload = {
      'api_key': API_KEY,
      'method': 'track.getInfo',
      'format': 'json'
      }
  r = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={artist_name}&track={song_name}&format=json', headers=headers, params=payload)
  result = json.loads(r.content)
  
  try:
     listener_count = result['track']['listeners']
  except:
     listener_count = 0

  try:
     playcount = result['track']['playcount']
  except:
     playcount = 0

  try:
     genre = result['track']['toptags']['tag'][0]['name']
  except:
     genre = 'No available genre tag'


  return song_name, artist_name, genre, playcount, listener_count


"""Create_genre_table_lastfm takes in as an argument song_info_lst, a compiled list of tuples which contain all relevant data pulled from get_track_info 
and the database, and creates the lastfm_genre_tags table which houses the unique genre tags pulled by the API data search and extraction in get_track_info. 
Uses an accumulator to create unique id's for each unique genre"""


def create_genre_table_lastfm(song_info_lst, database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()
   cur.execute('CREATE TABLE IF NOT EXISTS lastfm_genre_tags (id INTEGER UNIQUE, genre_tag TEXT UNIQUE)')

   accum = 1
   accum_lst = []
   for i in song_info_lst:
      if i[2] not in accum_lst:
         cur.execute('INSERT OR IGNORE into lastfm_genre_tags (id, genre_tag) VALUES(?, ?)', (accum, i[2]))
         accum += 1
         accum_lst.append(i[2])
   conn.commit()
   conn.close()




"""Add_info_to_database takes in an id_number, a tuple of song information, and the creates 'lastfm_songs' table in the database which represents the main table 
for data collected on last fm songs, The data is constructed in away so that there is no duplicate string data. The columns in this table are the generated song id, 
song name, artist name (represented by id's from spot_artists table, genre_id (represented by id's from spot_genres table) add a row of tuple song data to the database, using id's to not have duplicate string data"""


def add_info_to_database(id_num, song_info, database):
    #connecting to DB
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + database)
    cur = conn.cursor()

    cur.execute(f'SELECT id FROM spot_artists WHERE artist_name = "{song_info[1]}"')
    artist_id = cur.fetchone()[0]


    cur.execute(f'SELECT id FROM lastfm_genre_tags WHERE genre_tag = "{song_info[2]}"')
    genre_id = cur.fetchone()[0]

    #print(f'Adding {song_info[0]} into db')
    cur.execute('CREATE TABLE IF NOT EXISTS lastfm_songs (id INTEGER, name TEXT UNIQUE, artist_id INTEGER, genretag_id INTEGER, play_counts INTEGER, listener_counts INTEGER)')
    cur.execute('INSERT OR IGNORE INTO lastfm_songs (id,name,artist_id,genretag_id,play_counts,listener_counts) VALUES(?,?,?,?,?,?)', (id_num, song_info[0], artist_id, genre_id, song_info[3],
                                                                                                                  song_info[4]))                                                                                                    
    conn.commit()
    conn.close()



  

  
   

  #return result
   
 #/2.0/?method=album.gettoptags&artist=radiohead&album=the%20bends&api_key={API_KEY}&format=json
#/2.0/?method=tag.getTopTags&api_key={API_KEY}&format=json

def main():
  songs_list = [
      ("Shape of You", "Ed Sheeran", "÷ (Divide)", "Pop"),
      ("Blinding Lights", "The Weeknd", "After Hours", "R&B"),
      ("Happier", "Marshmello", "Joytime III", "EDM"),
      ("Uptown Funk", "Mark Ronson", "Uptown Special", "Pop"),
      ("Hello", "Adele", "25", "Soul"),
      ("Radioactive", "Imagine Dragons", "Night Visions", "Alternative Rock"),
      ("Sicko Mode", "Travis Scott", "Astroworld", "Hip Hop"),
      ("God's Plan", "Drake", "Scorpion", "Hip Hop"),
      ("Lose Yourself", "Eminem", "8 Mile (Soundtrack)", "Hip Hop"),
      ("Hotline Bling", "Drake", "Views", "Hip Hop"),
      ("Empire State of Mind", "Jay-Z", "The Blueprint 3", "Hip Hop"),
      ("In Da Club", "50 Cent", "Get Rich or Die Tryin'", "Hip Hop"),
      ("Gold Digger", "Kanye West", "Late Registration", "Hip Hop"),
      ("Can't Tell Me Nothing", "Kanye West", "Graduation", "Hip Hop"),
      ("Rolling in the Deep", "Adele", "21", "Pop"),
      ("Billie Jean", "Michael Jackson", "Thriller", "Pop"),
      ("I Will Always Love You", "Whitney Houston", "The Bodyguard: Original Soundtrack Album", "R&B"),
      ("Don't Stop Believin'", "Journey", "Escape", "Rock"),
      ("Someone Like You", "Adele", "21", "Pop"),
      ("Love Yourself", "Justin Bieber", "Purpose", "R&B"),
      ("Firework", "Katy Perry", "Teenage Dream", "Pop"),
      ("Call Me Maybe", "Carly Rae Jepsen", "Kiss", "Pop"),
      ("Cheap Thrills", "Sia", "This Is Acting", "Pop"),
      ("We Found Love", "Rihanna", "Talk That Talk", "Pop"),
      ("Can't Feel My Face", "The Weeknd", "Beauty Behind the Madness", "R&B"),
      ("Shake It Off", "Taylor Swift", "1989", "Pop"),
      ("Sugar", "Maroon 5", "V", "Pop, Funk"),
      ("Sorry", "Justin Bieber", "Purpose", "Pop, Dance"),
      ("Blank Space", "Taylor Swift", "1989", "Pop"),
      ("Viva La Vida", "Coldplay", "Viva la Vida or Death and All His Friends", "Pop"),
      ("My Universe", "Coldplay", "My Universe", "Genre"),
      ("Afterglow", "THE DRIVER ERA"),
      ("FADE", "THE DRIVER ERA"),
      ("Telepath", "Conan Gray"),
      ("Santiago", "jame minogue"),
      ("Take Me Higher", "A.C.E"),
      ("Papacito", "Alaina Castillo"),
      ("Greedy", "Ariana Grande"),
      ("Smokin Out The Window", "Bruno Mars"),
      ("Crash My Car", "Coin"),
      ("Shoot Me", "DAY 6"),
      ("Circles", "Post Malone"),
      ("Candle Flame", "Jungle"),
      ("Miracle", "Kimbra"),
      ("Cherry Flavoured", "The Neighborhood"),
      ("Movin Out (Anthony’s Song)", "Billy Joel"),
      ("Sexy Villain", "Remi Wolf"),
      ("Fantasy", "Mariah Carey"),
      ("Charlie Brown Theme", "Vince Guaraldi"),
      ("Ten Duel Commandments", "Lin Manuel Miranda"),
      ("What it Is", "Amber Mark"),
      ("Overnight", "Parcels"),
      ("Blitz", "Sferro"),
      ("Colours", "Roosevelt"),
      ("The Walk", "Mayer Hawthorne"),
      ("On the Floor", "Mayer Hawthorne"),
      ("Godzilla", "Eminem"),
      ("still feel", "half alive"),
      ("Skyfall", "Adele"),
      ("TEXAS HOLD ‘EM", "Beyoncé"),
      ("Simulation", "Tkay Maidza"),
      ("Dance Moves", "Franc Moody"),
      ("She Wants to Move", "N.E.R.D."),
      ("Don’t Start Now", "Dua Lipa"),
      ("Take Five", "Dave Brubeckcc Quartet"),
      ("Stairway to Heaven", "Led Zeppelin"),
      ("Hallelujah", "Jeff Buckley"),
      ("Clair de Lune", "Claude Debussy"),
      ("Green Onions", "Booker T. & the M.G’s"),
      ("How Far I’ll Go", "Auli’i Cravalho"),
      ("Cashmere", "Tkay Maidza"),
      ("Say So", "Doja Cat"),
      ("Heartless", "Kanye West"),
      ("Come Through", "H.E.R."),
      ("BMO", "Ari Lennox"),
      ("Boo'd Up", "Ella Mai"),
      ("No Guidance", "Chris Brown"),
      ("Cranes in the Sky", "Solange"),
      ("Location", "Khalid"),
      ("Future Nostalgia", "Dua Lipa"),
      ("Best Part", "Daniel Caesar"),
      ("Damage", "H.E.R."),
      ("Slide", "H.E.R."),
      ("Insecure", "Jazmine Sullivan"),
      ("Trip", "Ella Mai"),
      ("Focus", "H.E.R."),
      ("Lights On", "H.E.R."),
      ("Come Through and Chill", "Miguel"),
      ("Waves", "Normani ft. 6LACK"),
      ("Exchange", "Bryson Tiller"),
      ("Playing Games", "Summer Walker"),
      ("Post to Be", "Omarion"),
      ("Boo'd Up (Remix)", "Ella Mai"),
      ("Stay Ready (What a Life)", "Jhené Aiko"),
      ("Get Lucky", "Daft Punk"),
      ("Free", "6LACK"),
      ("My Affection", "Summer Walker"),
      ("Summertime Magic", "Childish Gambino"),
      ("Make Me Feel", "Janelle Monáe"),
      ("Yummy", "Justin Bieber")
      
      ]
  database = input("Enter the name of the database here: ")
  #'API_Audio_FusionDB.db'
  API_KEY = get_lastfm_API_KEY('LastFMAPI_KEY.txt')


  full_song_lst = []
  for song in songs_list:
   #tuple of song info, has song name, artist, genre(s), song popularity, explicit
      song_info = get_track_info(API_KEY, song[0], song[1])
      full_song_lst.append(song_info)
 
  create_genre_table_lastfm(full_song_lst, database)


    #database loads
  print('Loading the first 25 rows of data into db!')
  print('\n\n')
  accum_1 = 1
  data_load_1 = full_song_lst[:25]
  for song_info in data_load_1:
    add_info_to_database(accum_1, song_info,database)
    accum_1 += 1
      
  print('Loading the second batch of 25 data rows into db!')
  accum_2 = 26
  data_load_2 = full_song_lst[25:50]
  for song_info in data_load_2:
    add_info_to_database(accum_2, song_info,database)
    accum_2 += 1    
      

  print('Loading the third batch of 25 data rows into db!')
  accum_3 = 51
  data_load_3 = full_song_lst[50:75]
  for song_info in data_load_3:
    add_info_to_database(accum_3, song_info,database)
    accum_3 += 1   
      
  print('Loading the fourth batch of 25 data rows into db!')
  accum_4 = 76
  data_load_4 = full_song_lst[75: ]
  for song_info in data_load_4:
    add_info_to_database(accum_4, song_info,database)
    accum_4 += 1   







if __name__ == "__main__":
    main()



