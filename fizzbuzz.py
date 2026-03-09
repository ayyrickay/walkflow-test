"""Basic FizzBuzz implementation printing numbers from 1 to 100.

For multiples of 3, prints 'Fizz'.
For multiples of 5, prints 'Buzz'.
For multiples of both 3 and 5, prints 'FizzBuzz'.
Otherwise, prints the number itself.
"""

def fizzbuzz(start=1, end=100):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


if __name__ == "__main__":
    fizzbuzz()
