"""
FizzBuzz Example

Prints numbers from 1 to 100 with the following substitutions:
- "Fizz" for multiples of 3
- "Buzz" for multiples of 5
- "FizzBuzz" for multiples of both 3 and 5
"""

def fizzbuzz(n=100):
    for i in range(1, n + 1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        print(output or i)

if __name__ == '__main__':
    fizzbuzz()
