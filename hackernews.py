import requests
response =requests.get(" https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
print(response.json())