'''
JSON 파싱

json.loads: JSON 문자열을 Python 객체(딕셔너리)로 변환
'''

import json

# JSON 문자열
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON 문자열을 Python 객체로 변환
data = json.loads(json_data)

# Python 객체 출력
print(data)
print(type(data))