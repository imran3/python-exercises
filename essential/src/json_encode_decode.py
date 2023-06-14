import json
from json import JSONDecodeError, JSONEncoder

def parseJson(jsonString):
    try:
        res = json.loads(jsonString)
        return res
    except JSONDecodeError as e:
        print(e)

def toJson(inputObject):
    return json.dumps(inputObject)

# test
myJson = '{"name": "John Smith","age": 30,"city": "New York","email": "johnsmith@example.com"}'
res = parseJson(myJson)
print(toJson(res))



# custom encoder
class Car:
    def __init__(self, model):
        self.model = model

class CarJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Car):
            return o.model
        return super().default(0)
    
# test customer encoder
carsDict = {'a': Car('Audio'), 'b': Car('BMW'), 'T': Car('Toyota')}
print(json.dumps(carsDict, cls=CarJSONEncoder))