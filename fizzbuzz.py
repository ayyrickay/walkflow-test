"""
Simple FizzBuzz example script.

This script prints numbers from 1 to 100 with the following rules:
- For multiples of 3, print 'Fizz'
- For multiples of 5, print 'Buzz'
- For multiples of both 3 and 5, print 'FizzBuzz'

This example serves as a minimal demonstration of basic workflow functionality.
"""

def fizzbuzz(n=100):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    fizzbuzz()
