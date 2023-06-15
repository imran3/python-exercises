import pytest
from src.hex_to_dec import hex_to_dec

@pytest.mark.parametrize('hex_num, expected_dec', [('', 0),('1A', 26), ('123', 291),('E1F2BA', 14807738), ('aBc', 2748), ('124BBCDFE', 4911255038)])
def test_valid_hexadecimal(hex_num, expected_dec):
    assert hex_to_dec(hex_num) == expected_dec

@pytest.mark.parametrize('hex_num', ['G', 'XYZ', '$!%'])
def test_invalid_hexadecimal(hex_num):
    assert hex_to_dec(hex_num) is None

@pytest.mark.parametrize('hex_num', [123, ['A', 'B', 'C']])
def test_non_string_input(hex_num):
    assert hex_to_dec(hex_num) is None