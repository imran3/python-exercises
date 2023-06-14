import json
from src.json_encode_decode import decodeJSON, encodeJSON, Car, CarJSONEncoder

def test_decodeJSON_valid():
    input = myJson = '{"name": "John Smith","age": 30,"city": "New York","email": "johnsmith@example.com"}'
    expected = {"name": "John Smith","age": 30,"city": "New York","email": "johnsmith@example.com"}
    res = decodeJSON(input)
    assert res == expected

def test_decodeJSON_invalid():
    input = '{"name": Invalid JSON, "New York" "email": 123}'
    expected = "Input is not valid JSON"
    res = decodeJSON(input)
    assert res == expected

def test_encodeJSON():
    input = {"name": "John Smith","age": 30,"city": "New York"}
    expect = '{"name": "John Smith", "age": 30, "city": "New York"}'
    res = encodeJSON(input)
    assert res == expect

def test_CarJSONEncoder():
    carsDict = {'a': Car('Audi'), 'b': Car('BMW'), 'T': Car('Toyota')}
    expected = '{"a": "Audi", "b": "BMW", "T": "Toyota"}'
    res = json.dumps(carsDict, cls=CarJSONEncoder)
    assert res == expected