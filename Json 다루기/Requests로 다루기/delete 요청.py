import requests

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.text)
print(response.status_code)
