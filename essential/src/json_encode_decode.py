import json
from json import JSONDecodeError, JSONEncoder

def decodeJSON(jsonString):
    try:
        res = json.loads(jsonString)
        return res
    except JSONDecodeError:
        return "Input is not valid JSON"

def encodeJSON(inputObject):
    return json.dumps(inputObject)

class Car:
    def __init__(self, model):
        self.model = model

# custom encoder
class CarJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Car):
            return o.model
        return super().default(0)