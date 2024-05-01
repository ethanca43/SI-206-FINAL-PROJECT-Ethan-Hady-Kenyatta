from dotenv import load_dotenv
import requests
import json
import os
import sqlite3

"""receive_access_token sends over to Spotify servers our client id and secret id to receive back a response that contains within it our access token, aka our API Key so that we may process the spotify json data"""
def receive_access_token(client_id, client_secret):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret}
    response = requests.post('https://accounts.spotify.com/api/token', data=data)

    result =json.loads(response.content)
    return result['access_token']
    

"""oauth_header creates a header that will be required for future api calls. They are an arguement required for any requests.get call, as well a params"""

def oauth_header(token):
  headers = {'Authorization': f'Bearer {token}'}
  return headers



"""track_search takes in the token received from 'receive_access_token', any track name, and any track artist name, and then tretrieves the first listed search result on spotify returning the name requested, the artist request and their
 (genre, track_popularity, explicit, album) for the requested song and artist. Also returns song name and artist name originally inputted."""

def track_search(token, track_name,artist_name):
    url = f'https://api.spotify.com/v1/search'
    header = oauth_header(token)
    params = {
    'q': f'{track_name}%{artist_name}',
    'type': 'track,artist'}
    response = requests.get(url, params=params, headers=header).json()

    album = response['tracks']['items'][0]['album']['name']

    if len(response['artists']['items']) > 0 and len(response['artists']['items'][0]['genres']) > 0:
      genre = response['artists']['items'][0]['genres'][0]
    else:
      genre = 'No listed Genre'

    track_popularity = response['tracks']['items'][0]['popularity']

    explicit = response['tracks']['items'][0]['explicit']
    if explicit == True:
      explicit = 1
    else: 
      explicit = 2
    return track_name, artist_name, genre, track_popularity, explicit, album

"""Create_artists_table takes song_lst, a list of songs in which each song is represented as a tuple containing the song name and aritst name, and the database, 
creates the table 'spot_artists' in the database and loops thru the the provided list adding unique ids with unique artists to the newly created table"""

def create_artists_table(song_lst, database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()
   cur.execute('CREATE TABLE IF NOT EXISTS spot_artists (id INTEGER UNIQUE, artist_name TEXT UNIQUE)')
   accum = 1
   accum_lst = []
   for i in song_lst:
      if i[1] not in accum_lst:
         cur.execute('INSERT OR IGNORE into spot_artists (id, artist_name) VALUES(?, ?)', (accum, i[1]))
         accum += 1
         accum_lst.append(i[1])
   conn.commit()
   conn.close()



"""Create_albums_table takes in song_info_lst, a compiled list of tuples which contain all relevant data pulled from track_id_search, and the database,
 then creates the table 'albums' which, similarly to create_artists table, loops thru the data of the songs in a list adds the unique albums and their unique id nums to the table"""

def create_albums_table(song_info_lst, database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()
   cur.execute('CREATE TABLE IF NOT EXISTS albums (id INTEGER UNIQUE, album_name TEXT UNIQUE)')

   accum = 1
   accum_lst = []
   for i in song_info_lst:
      if i[-1] not in accum_lst:
         cur.execute('INSERT OR IGNORE into albums (id, album_name) VALUES(?, ?)', (accum, i[-1]))
         accum += 1
         accum_lst.append(i[-1])
   conn.commit()
   conn.close()

"""Create_genre_table takes in song_info_lst, a compiled list of tuples which contain all relevant data pulled from track_id_search, and the database,
then creates the table 'spotify_genres'. It then loops thru the provided list extracting the album information, and adding unique albums with a unique id assigned to spotify_genres table """


def create_genre_table(song_info_lst, database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()
   cur.execute('CREATE TABLE IF NOT EXISTS spotify_genres (id INTEGER UNIQUE, genre_name TEXT UNIQUE)')

   accum = 1
   accum_lst = []
   for i in song_info_lst:
      if i[2] not in accum_lst:
         cur.execute('INSERT OR IGNORE into spotify_genres (id, genre_name) VALUES(?, ?)', (accum, i[2]))
         accum += 1
         accum_lst.append(i[2])
   conn.commit()
   conn.close()

"""Create_explicit_tables takes in only the database as its argument and makes a subtable 'explicit' for explicitness in spotify songs. 
1 represents yes, the song is explicit, and 2, represents, no the song is not explict.  """


def create_explicit_tables(database):
   path = os.path.dirname(os.path.abspath(__file__))
   conn = sqlite3.connect(path + "/" + database)
   cur = conn.cursor()

   cur.execute('CREATE TABLE IF NOT EXISTS explicit (id INTEGER UNIQUE, explicitness TEXT UNIQUE)')
   cur.execute('INSERT INTO explicit (id, explicitness) VALUES(?,?)', (1, 'Yes'))
   cur.execute('INSERT INTO explicit (id, explicitness) VALUES(?,?)', (2, 'No'))
   conn.commit()
   conn.close()



"""Add_info_to_database takes in an id_number, a tuple of song information, and the creates 'spotify_songs' table in the database which represents the main table 
for data collected on spotify songs, The data is constructed in away so that there is no duplicate string data. The columns in this table are the generated song id, 
song name, artist name (represented by id's from spot_artists table, genre_id (represented by id's from spot_genres table) add a row of tuple song data to the database, using id's to not have duplicate string data"""


def add_info_to_database(id_num, song_info, database):
    #connecting to DB
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + database)
    cur = conn.cursor()

    cur.execute(f'SELECT id FROM spot_artists WHERE artist_name = "{song_info[1]}"')
    artist_id = cur.fetchone()[0]

    cur.execute(f'SELECT id FROM albums WHERE album_name = "{song_info[-1]}"')
    album_id = cur.fetchone()[0]

    cur.execute(f'SELECT id FROM spotify_genres WHERE genre_name = "{song_info[2]}"')
    genre_id = cur.fetchone()[0]

    #print(f'Adding {song_info[0]} into db')
    cur.execute('CREATE TABLE IF NOT EXISTS spotify_songs (id INTEGER, name TEXT UNIQUE, artist_id INTEGER, genre_id INTEGER, song_popularity INTEGER, explicit_id INTEGER, album_id INTEGER)')
    cur.execute('INSERT OR IGNORE INTO spotify_songs (id,name,artist_id,genre_id,song_popularity,explicit_id,album_id) VALUES(?,?,?,?,?,?,?)', (id_num, song_info[0], artist_id, genre_id, song_info[3],
                                                                                                                  song_info[4],album_id))                                                                                                    
    conn.commit()
    conn.close()




def main():

   load_dotenv()
   client_id = os.getenv("CLIENT_ID")  
   client_secret = os.getenv("SECRET_CLIENT")

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
   #database = 'API_Audio_FusionDB.db'
   token = receive_access_token(client_id, client_secret)
   database = input("Enter the name of the database here: ")

   create_artists_table(songs_list,database)
   create_explicit_tables(database)

   
   full_song_lst = []
   #gathering data from Spotify API to compile into full_song_lst
   for song in songs_list:
   #    #tuple of song info, has song name, artist, genre(s), song popularity, explicit
      song_info = track_search(token, song[0], song[1])
      full_song_lst.append(song_info)

   #create the albums and genre table
   create_albums_table(full_song_lst, database)
   create_genre_table(full_song_lst, database)

   #database loads
   print('Loading the first 25 rows of data into db!')
   print('\n\n')
   accum_1 = 1
   data_load_1 = full_song_lst[:25]
   for song_info in data_load_1:
      add_info_to_database(accum_1, song_info,database)
      accum_1 += 1
      


   print('Loading the second batch of 25 data rows into db!')
   print('\n\n')
   accum_2 = 26
   data_load_2 = full_song_lst[25:50]
   for song_info in data_load_2:
      add_info_to_database(accum_2, song_info,database)
      accum_2 += 1    
      

   print('Loading the third batch of 25 data rows into db!')
   print('\n\n')
   accum_3 = 51
   data_load_3 = full_song_lst[50:75]
   for song_info in data_load_3:
      add_info_to_database(accum_3, song_info,database)
      accum_3 += 1   
      
   print('Loading the fourth batch of 25 data rows into db!')
   print('\n\n')
   accum_4 = 76
   data_load_4 = full_song_lst[75: ]
   for song_info in data_load_4:
      add_info_to_database(accum_4, song_info,database)
      accum_4 += 1   


   # for song_info in full_song_lst:
   #    add_info_to_database(accum, song_info,'API_Audio_FusionDB.db')
   #    accum += 1
 
  

if __name__ == "__main__":
    main()