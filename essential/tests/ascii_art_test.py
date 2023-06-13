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

def test_decode():
    input = [('A', 1), ('X', 3), (' ', 1), ('Q', 2), ('&', 5), ('\n', 2), ('P',6)]
    expected = '''AXXX QQ&&&&&\n\nPPPPPP'''
    res = decode_art(input)
    assert res == expected

def test_decode_empty():
    input = []
    expected = ''
    res = decode_art(input)
    assert res == expected

def test_encode_valid_multiline():
    input = '''
          .
         _|_
        |===|
        |===|
        |===|
        |===|
        '---'''
    expected = [('\n', 1), (' ', 10), ('.', 1), ('\n', 1), (' ', 9), ('_', 1), ('|', 1), ('_', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ("'", 1), ('-', 3)]
    res = encode_art(input)
    assert res == expected

def test_decode_valid_multiline():
    input = [('\n', 1), (' ', 10), ('.', 1), ('\n', 1), (' ', 9), ('_', 1), ('|', 1), ('_', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ('|', 1), ('=', 3), ('|', 1), ('\n', 1), (' ', 8), ("'", 1), ('-', 3)]
    expected = '''
          .
         _|_
        |===|
        |===|
        |===|
        |===|
        '---'''
    res = decode_art(input)
    print(res)
    assert res == expected