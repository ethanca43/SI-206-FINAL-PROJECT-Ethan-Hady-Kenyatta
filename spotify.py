from dotenv import load_dotenv
import requests
import json
import os
import curl

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("SECRET_CLIENT")
def receive_access_token():
    print(client_id, client_secret)

    url = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret}
    response = requests.post('https://accounts.spotify.com/api/token', data=data)

    result =json.loads(response.content)
    #print(result['access_token'])
    return result['access_token']
    
token = receive_access_token()
print(token)

def oauth_header(token):
  headers = {'Authorization': f'Bearer {token}'}
  return headers



def get_artist(token):
   url = 'https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb'
   header = oauth_header(token)
   response = requests.get(url, headers=header)

   print(response.json())


get_artist(token)

# headers = {
#     'Authorization': 'Bearer NgCXRK...MzYjw',
# }




#curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" \
     #-H "Authorization: Bearer  BQCdFGmtesiEdzZ3_l1mUxq_xyTFMiueAT010BUAjriMy_mtsUn47Zk0OEhfGoTwe200LDlhbAIRjN5PTWp05S606eWzfcayW_tXsGqGxlZxgPobOKc"