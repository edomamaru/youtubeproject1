import requests
data={
  'title': 'Special Agent',
  'body': 'Leroy Jethro Gibbs',
  'userId': '1'
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)

print( response.status_code)
print(response.json())
