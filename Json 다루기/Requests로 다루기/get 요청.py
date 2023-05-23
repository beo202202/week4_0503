import requests
from pprint import pprint

response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.headers)
# print(response.content)
print(response.text)
# pprint(response.json())
# print(response.status_code)
