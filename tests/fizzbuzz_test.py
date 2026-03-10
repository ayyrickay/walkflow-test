"""
Unit tests for the FizzBuzz problem.

These tests verify the correctness of a FizzBuzz implementation.

Rules tested:
- Numbers divisible by 3 return "Fizz"
- Numbers divisible by 5 return "Buzz"
- Numbers divisible by both 3 and 5 return "FizzBuzz"
- Other numbers return their string representation

Usage:
- Implement a function `fizzbuzz(n: int) -> str` in your code.
- Run these tests with pytest to validate your implementation.

Note: The FizzBuzz function is not implemented here.
"""
import pytest

# The tests expect a function fizzbuzz(n) to be implemented by the user.
# To run tests, implement fizzbuzz(n) in your codebase.

@pytest.mark.parametrize("input_value,expected_output", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, "7"),
    (8, "8"),
    (9, "Fizz"),
    (10, "Buzz"),
    (11, "11"),
    (12, "Fizz"),
    (13, "13"),
    (14, "14"),
    (15, "FizzBuzz"),
])
def test_fizzbuzz(input_value, expected_output):
    """Test fizzbuzz output for given input values."""
    # Import fizzbuzz function here to allow user implementation
    from fizzbuzz import fizzbuzz
    assert fizzbuzz(input_value) == expected_output
