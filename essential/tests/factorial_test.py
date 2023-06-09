import pytest
from src.factorial import factorial, factorial_recursive

@pytest.fixture
def input_expected_pairs(): return [(5, 120), (6, 720), (0, 1), (-2, None), (1.2, None), ('invalid input', None), (None, None)]

def test_factorial(input_expected_pairs):
    for input, expected in input_expected_pairs:
        res = factorial(input)
        assert res == expected


def test_factorial_recursive(input_expected_pairs):
    for input, expected in input_expected_pairs:
        res = factorial_recursive(input)
        assert res == expected