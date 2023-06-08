import pytest
from src.transform_string import hacker_speak

def test_hacker_speak_replace():
    input = "this is so cool!"
    expected = "th15 15 50 c00l!"
    res = hacker_speak(input)
    assert res == expected

def test_hacker_speak_replace_all():
    input = "aaaeeeiiiioooss ssiii eeeooo sssaa aeios"
    expected = "444333111100055 55111 333000 55544 43105"
    res = hacker_speak(input)
    assert res == expected

def test_hacker_speak_no_replace():
    input = "Fly thy crypt!"
    expected = "Fly thy crypt!"
    res = hacker_speak(input)
    assert res == expected