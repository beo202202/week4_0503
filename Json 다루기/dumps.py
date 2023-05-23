'''json.dumps: Python 객체를 JSON 문자열로 변환'''

import json

# Python 객체
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Python 객체를 JSON 문자열로 변환
json_data = json.dumps(data)

# JSON 문자열 출력
print(json_data)
print(type(json_data))
