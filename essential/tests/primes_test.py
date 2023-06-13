from src.primes import primesUpTo

def test_primes_valid_input():
    input = 101
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    res = primesUpTo(input)
    assert res == expected

def test_primes_negative_input():
    assert primesUpTo(-10) == None

def test_primes_input_one():
    assert primesUpTo(1) == []