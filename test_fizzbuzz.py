import pytest

# Example FizzBuzz implementation to test
# Users can replace this with their own implementation

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

@pytest.mark.parametrize("input,expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (45, "FizzBuzz"),
    (98, "98"),
    (99, "Fizz"),
    (100, "Buzz"),
])
def test_fizzbuzz(input, expected):
    assert fizzbuzz(input) == expected


def test_fizzbuzz_range():
    # Test the entire range 1 to 100 for no exceptions and correct types
    for i in range(1, 101):
        result = fizzbuzz(i)
        assert isinstance(result, str)
        # Check correct output for multiples
        if i % 15 == 0:
            assert result == "FizzBuzz"
        elif i % 3 == 0:
            assert result == "Fizz"
        elif i % 5 == 0:
            assert result == "Buzz"
        else:
            assert result == str(i)
