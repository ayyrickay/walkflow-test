"""FizzBuzz implementation printing numbers 1 to 100 with substitutions:
- Multiples of 3: 'Fizz'
- Multiples of 5: 'Buzz'
- Multiples of both 3 and 5: 'FizzBuzz'

Run this script directly to see the output.
"""

def fizzbuzz():
    for i in range(1, 101):
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
