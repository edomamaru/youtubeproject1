import requests

response= requests.get('http://api.open-notify.org/astros.json')

print(response.status_code)

data = response.json()

names =[person['name'] for person in data['people']]

for i in names[:5]:
  print(i)