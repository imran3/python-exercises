import pytest
from src.sort_dictionary import sort_contacts_list, sort_contacts_list_v2

def test_sort_contacts_list():
    input = {"124": "mark", "435": "John", "4526": "Andrew", "4527": "Jacob"}
    expected = ["Andrew", "Jacob", "John", "mark"]

    res = sort_contacts_list(input)
    print(res)
    assert res == expected

def test_sort_contacts_list_v2():
    input = {"124": "mark", "435": "John", "4526": "Andrew", "4527": "Jacob"}
    expected = ["Andrew", "Jacob", "John", "mark"]

    res = sort_contacts_list_v2(input)
    print(res)
    assert res == expected