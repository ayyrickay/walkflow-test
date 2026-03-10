"""
FizzBuzz Example

This script prints the numbers from 1 to 100.
For multiples of three, it prints "Fizz" instead of the number.
For multiples of five, it prints "Buzz" instead of the number.
For numbers which are multiples of both three and five, it prints "FizzBuzz".

This example serves as a simple demonstration and testing asset.
"""

def fizzbuzz(n=100):
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
