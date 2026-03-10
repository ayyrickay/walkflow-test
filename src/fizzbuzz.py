"""Fizzbuzz implementation: prints numbers 1 to 100 with substitutions.

- For multiples of 3, prints 'Fizz'
- For multiples of 5, prints 'Buzz'
- For multiples of both 3 and 5, prints 'Fizzbuzz'
"""

def fizzbuzz():
    for i in range(1, 101):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        print(output or i)


if __name__ == '__main__':
    fizzbuzz()
