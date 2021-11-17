import json
object_ = {
    "name":"David",
    "class":1,
    "age":6
}
print(type(object_))
json_object = json.dumps(object_)
print(type(json_object))
