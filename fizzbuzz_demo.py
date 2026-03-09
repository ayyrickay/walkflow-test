"""
Simple FizzBuzz Demo Script

Prints numbers from 1 to 100 with the following rules:
- Multiples of 3 print "Fizz"
- Multiples of 5 print "Buzz"
- Multiples of both 3 and 5 print "FizzBuzz"

Run this script to see the output in the console.
"""

def fizzbuzz(limit=100):
    """Print FizzBuzz from 1 to limit."""
    for num in range(1, limit + 1):
        output = ''
        if num % 3 == 0:
            output += 'Fizz'
        if num % 5 == 0:
            output += 'Buzz'
        print(output or num)


if __name__ == '__main__':
    fizzbuzz()
