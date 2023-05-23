import json
import requests

data = {"title": "homework", "body": "Lee Juneyoung", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)


response_dict = json.loads(response.text)
title = response_dict['title']
body = response_dict['body']
userId = response_dict['userId']
id = response_dict['id']


with open('result.txt', 'w') as result:
    result.write(f'{title}\n')
    result.write(f'{body}\n')
    result.write(f'{userId}\n')
    result.write(f'{str(id)}\n')