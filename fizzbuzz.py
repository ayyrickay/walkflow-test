"""FizzBuzz implementation.

Print numbers from 1 to 100 with the following rules:
- Multiples of 3 are replaced with 'Fizz'
- Multiples of 5 are replaced with 'Buzz'
- Multiples of both 3 and 5 are replaced with 'FizzBuzz'
"""

def fizzbuzz(n=100):
    """Print the FizzBuzz sequence from 1 to n inclusive."""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz()
