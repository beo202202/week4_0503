'''json.load: JSON 파일을 Python 객체(딕셔너리)로 변환'''

import json

# JSON 파일 읽기
with open('data.json') as file:
    data = json.load(file)

# Python 객체 출력
print(data)
print(type(data))

'''{
    "employee": {
        "name":       "sonoo",
        "salary":      56000,
        "married":    true
    }
}'''

print(data['employee'])
print(data['employee']['name'])
print(data['employee']['salary'])
