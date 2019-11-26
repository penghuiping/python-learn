import json

map = {"name": "jack", "age": 12}

jsonStr = json.dumps(map)

print(jsonStr)

map = json.loads(jsonStr)

print(map["name"])
