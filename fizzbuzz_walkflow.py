"""
FizzBuzz example illustrating the 'walk' (iteration) and 'flow' (conditional branching) concepts.
This script prints numbers from 1 to 100, substituting multiples of 3 with 'Fizz',
multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'.
"""

def fizzbuzz_walkflow(start=1, end=100):
    """Walk through numbers from start to end and flow through conditions to print FizzBuzz."""
    for number in range(start, end + 1):  # Walk: iterate through the sequence
        output = ''
        if number % 3 == 0:  # Flow: condition for multiples of 3
            output += 'Fizz'
        if number % 5 == 0:  # Flow: condition for multiples of 5
            output += 'Buzz'
        print(output or number)


if __name__ == '__main__':
    fizzbuzz_walkflow()
