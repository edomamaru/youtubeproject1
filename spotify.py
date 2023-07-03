import requests
import os

AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
'grant_type': 'client_credentials',
'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
print (headers)
print(auth_response_data)
BASE_URL = 'https://api.spotify.com/v1/'
track_id = '6mFkJmJqdDVQ1REhVfGgd1'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

print(r.json())

