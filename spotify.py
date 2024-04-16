from dotenv import load_dotenv
import requests
import json
import os
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

#def 


#https://api.spotify.com/browse/new-releases'
def main():
  token = receive_access_token()
  headers = oauth_header(token)
  get_artist(token)
  get_new_releases(token)

if __name__ == "__main__":
    main()