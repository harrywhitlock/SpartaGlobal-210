import json


with open('generated.json', 'r') as f:

    data = json.load(f)

print(data)

#json_file = json.dump(data)

test_dict = {"name": "Lillian",
             "age": 27,
             "city" : "New York"}

json_file_test = json.dumps(test_dict)
with open('newjson.json', 'w') as d:
        json.dump(json_file_test, d)

json_string = json.dumps(data)

data2 = json.loads(json_string)

print(data2)