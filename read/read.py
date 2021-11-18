import json

with open('movies.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)
print(obj)
print(obj["Name"])