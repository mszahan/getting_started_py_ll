import json
from json import JSONDecodeError,JSONEncoder


## json to python dictionary
json_string = '{"a": "apple", "b": "bear", "c": "cat",}'
# data = json.loads(json_string)
## to avoid decode error use try and except
try:
    json.loads(json_string)
except JSONDecodeError:
    print('Could not parse JSON')


## python dictionary to json

python_dict = {"a": "apple", "b": "bear", "c": "cat",}
data = json.dumps(python_dict)
# print(data)



###------------------------
## custom encoder 
###---------------------

class Animal:
    def __init__(self, name):
        self.name = name

## now creating a new JSON encoder
class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)

py_dict = {"a": Animal('advark'), "b": Animal('bear'), "c": Animal('cat')}


json.dumps(py_dict, cls=AnimalEncoder)



