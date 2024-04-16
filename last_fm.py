from dotenv import load_dotenv
import requests
import json
import os
import curl


def get_lastfm_API_KEY(filename):
  base_path = os.path.abspath(os.path.dirname(__file__))
  full_path = os.path.join(base_path, filename)
  with open(full_path, 'r') as f:
     API_KEY = f.read()
     print(API_KEY)
  return API_KEY


# headers = {
#     'user-agent': 'ethanca43'
# }

#r = requests.get('https://my-api-url', headers=headers)
def request_top_artists(API_KEY):
  headers = {
      'user-agent': 'ethanca43'
  }
  payload = {
      'api_key': API_KEY,
      'method': 'chart.gettopartists',
      'format': 'json'
  }
  r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
 #print(r.status_code)
  result = json.loads(r.content)
  #print(result)
  return result

def request_top_tags(API_KEY):
  headers = {
      'user-agent': 'ethanca43'
  }
  payload = {
      'api_key': API_KEY,
      'method': 'tag.getTopTags',
      'format': 'json'
  }
  r = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key={API_KEY}&format=json', headers=headers, params=payload)
 #print(r.status_code)
  result = json.loads(r.content)
  print(result)
  #return result
   
 #/2.0/?method=album.gettoptags&artist=radiohead&album=the%20bends&api_key={API_KEY}&format=json
#/2.0/?method=tag.getTopTags&api_key={API_KEY}&format=json

def main():
  API_KEY = get_lastfm_API_KEY('LastFMAPI_KEY.txt')
  request_top_artists(API_KEY)
  request_top_tags(API_KEY)


if __name__ == "__main__":
    main()



