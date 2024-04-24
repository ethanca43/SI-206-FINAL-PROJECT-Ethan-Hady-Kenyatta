from dotenv import load_dotenv
import requests
import json
import os
import sqlite3
import curl


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("SECRET_CLIENT")
def receive_access_token():
    #print(client_id, client_secret)

    url = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret}
    response = requests.post('https://accounts.spotify.com/api/token', data=data)

    result =json.loads(response.content)
    #print(result['access_token'])
    return result['access_token']
    
#print(token)

def oauth_header(token):
  headers = {'Authorization': f'Bearer {token}'}
  return headers



def get_artist(token):
   url = 'https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb'
   header = oauth_header(token)
   response = requests.get(url, headers=header)

   #print(response.json())


def get_new_releases(token):
   url = 'https://api.spotify.com/v1/browse/new-releases'
   header = oauth_header(token)
   response = requests.get(url, headers=header).json()
   #print(response.json())
   #print(response)

   

   n_d = []
    
   for release_d in response['albums']['items']:
      #print(release_d)
      #web_link = release_d['items']['artists'][0]['external_urls']['spotify']
      track_artists = {}
      for artist in release_d['artists']:
         name = artist['name']
         artist_id = artist['id']
         if name not in track_artists:
            track_artists[name] = artist_id

      #artist_name = release_d['artists'][0]['name']
      album_link = release_d['external_urls']['spotify']
      album_title = release_d['name']
      album_release_date = release_d['release_date']
      album_track_count = release_d['total_tracks']
      album_type = release_d['type']

  
      # print(album_link)
      # print(album_title)
      # print(album_release_date)
      # print(album_track_count)
      # print(album_type)
      # print('\n\n')

      n_d.append((album_title, track_artists, album_track_count, album_type, album_release_date, album_link, True))
   print(n_d)
   return n_d

def get_track_info(token, spotify_id):
   url = f'https://api.spotify.com/v1/tracks/{spotify_id}'
   header = oauth_header(token)
   response = requests.get(url, headers=header).json()
   #print(response)
   

#album_id_search
"""retrieves the first spotify Id for the requested album_name. To be used to request indiviual song data. We will want to capture 100 album id's"""

def track_id_search(token, track_name,artist_name):
    url = f'https://api.spotify.com/v1/search'
    header = oauth_header(token)
    params = {
    'q': f'{track_name}%{artist_name}',
    'type': 'track,artist'}
    response = requests.get(url, params=params, headers=header).json()
    track_id = response['tracks']['items'][0]['id']
    album = response['tracks']['items'][0]['album']['name']
    if len(response['artists']['items']) > 0:
      genre = response['artists']['items'][0]['genres']
      genre = '/'.join(genre)
    else:
      genre = None

   #  followers = response['artists']['items'][0]['followers']['total']
   # #  print(followers)
   #  artist_popularity = response['artists']['items'][0]['popularity']
   # #  print(artist_popularity)
   # #  print('\n\n')
   
    track_popularity = response['tracks']['items'][0]['popularity']  #int
    #print(track_popularity)
    explicit = response['tracks']['items'][0]['explicit']#boolean
    if explicit == True:
      explicit = 1
    else: 
      explicit = 2
   #print(explicit)

   #print(track_name, artist_name, genre, track_popularity, explicit, album)

    return track_name, artist_name, genre, track_popularity, explicit, album

def add_info_to_database(id_num, song_info, database):
    #connecting to DB
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + database)
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS spotify_songs (id INTEGER, name TEXT UNIQUE, artist TEXT, genre TEXT, song_popularity INTEGER, explicit INTEGER, album TEXT UNIQUE)')

    cur.execute('INSERT OR IGNORE INTO spotify_songs (id,name,artist,genre,song_popularity,explicit,album) VALUES(?,?,?,?,?,?,?)', (id_num, song_info[0], song_info[1], song_info[2], song_info[3],
                                                                                                                  song_info[4],song_info[5]))
                                                                                                                  
    conn.commit()


   #  return id, out_name, album_artists




# def get_album_info(token, id):
#     url = f'https://api.spotify.com/v1/albums/{id}/tracks'
#     header = oauth_header(token)
#     response = requests.get(url, headers=header).json()
#     print(response)

   #'39McjovZ3M6n5SFtNmWTdp'


#https://api.spotify.com/browse/new-releases'
def main():
   #so far 70/100 Songs
   songs_list = [
      ("Shape of You", "Ed Sheeran", "÷ (Divide)", "Pop"),
      ("Blinding Lights", "The Weeknd", "After Hours", "R&B"),
      ("Happier", "Marshmello ft. Bastille", "Joytime III", "EDM"),
      ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "Uptown Special", "Pop"),
      ("Hello", "Adele", "25", "Soul"),
      ("Radioactive", "Imagine Dragons", "Night Visions", "Alternative Rock"),
      ("Sicko Mode", "Travis Scott", "Astroworld", "Hip Hop"),
      ("God's Plan", "Drake", "Scorpion", "Hip Hop"),
      ("Lose Yourself", "Eminem", "8 Mile (Soundtrack)", "Hip Hop"),
      ("Hotline Bling", "Drake", "Views", "Hip Hop"),
      ("Empire State of Mind", "Jay-Z ft. Alicia Keys", "The Blueprint 3", "Hip Hop"),
      ("In Da Club", "50 Cent", "Get Rich or Die Tryin'", "Hip Hop"),
      ("Gold Digger", "Kanye West ft. Jamie Foxx", "Late Registration", "Hip Hop"),
      ("Can't Tell Me Nothing", "Kanye West", "Graduation", "Hip Hop"),
      ("Rolling in the Deep", "Adele", "21", "Pop"),
      ("Billie Jean", "Michael Jackson", "Thriller", "Pop"),
      ("I Will Always Love You", "Whitney Houston", "The Bodyguard: Original Soundtrack Album", "R&B"),
      ("Don't Stop Believin'", "Journey", "Escape", "Rock"),
      ("Someone Like You", "Adele", "21", "Pop"),
      ("Love Yourself", "Justin Bieber", "Purpose", "R&B"),
      ("Firework", "Katy Perry", "Teenage Dream", "Pop"),
      ("Call Me Maybe", "Carly Rae Jepsen", "Kiss", "Pop"),
      ("Cheap Thrills", "Sia ft. Sean Paul", "This Is Acting", "Pop"),
      ("We Found Love", "Rihanna ft. Calvin Harris", "Talk That Talk", "Pop"),
      ("Can't Feel My Face", "The Weeknd", "Beauty Behind the Madness", "R&B"),
      ("Shake It Off", "Taylor Swift", "1989", "Pop"),
      ("Sugar", "Maroon 5", "V", "Pop, Funk"),
      ("Sorry", "Justin Bieber", "Purpose", "Pop, Dance"),
      ("Blank Space", "Taylor Swift", "1989", "Pop"),
      ("Viva La Vida", "Coldplay", "Viva la Vida or Death and All His Friends", "Pop"),
      ("My Universe", "Coldplay & BTS", "My Universe", "Genre"),
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
      ("Charlie Brown Theme", "Vince Guaraldi Theme"),
      ("Ten Duel Commandments", "Lin Manuel Miranda, Jon Rua, Leslie Odom Jr."),
      ("What it Is", "Amber Mark"),
      ("Overnight", "Parcels"),
      ("Blitz", "Sferro"),
      ("Colours", "Roosevelt"),
      ("The Walk", "Mayer Hawthorne"),
      ("On the Floor", "Mayer Hawthorne"),
      ("Godzilla (feat. Juice WRLD)", "Eminem, Juice WRLD"),
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
      ("How Far I’ll Go", "Auli’i Cravalho")
      ]
   #print(songs_list)
   token = receive_access_token()
   headers = oauth_header(token)
#   get_artist(token)
#   get_new_releases(token)
   #track_id_search(token, 'In Da Club', '50 Cent')
   #get_track_info(token,'4RY96Asd9IefaL3X4LOLZ8')
   #add_info_to_database(1, bts_song, 'API_Audio_FusionDB.db')
  #get_album_info(token,'39McjovZ3M6n5SFtNmWTdp')
   accum = 1
   for song in songs_list:
   #    #tuple of song info, has song name, artist, genre(s), song popularity, explicit
      song_info = track_id_search(token, song[0], song[1])
      add_info_to_database(accum, song_info, 'API_Audio_FusionDB.db')
      accum += 1


  

if __name__ == "__main__":
    main()