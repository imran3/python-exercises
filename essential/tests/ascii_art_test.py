import pytest
from src.ascii_art import encode_art, decode_art

def test_encode_valid_input():
    input = 'AAABCCCCMMM  X'
    expected = [('A', 3), ('B', 1), ('C', 4), ('M', 3), (' ', 2), ('X', 1)]
    res = encode_art(input)
    assert res == expected

def test_encode_empty_string_input():
    input = ''
    expected = None
    res = encode_art(input)
    assert res == expected
    
def test_encode_invalid_input():
    input = 1244
    expected = None
    res = encode_art(input)
    assert res == expected

