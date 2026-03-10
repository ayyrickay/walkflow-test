"""
FizzBuzz Example Test Script

This script demonstrates the classic FizzBuzz problem,
printing numbers from 1 to 100 with substitutions:
- 'Fizz' for multiples of 3
- 'Buzz' for multiples of 5
- 'FizzBuzz' for multiples of both 3 and 5

This example serves to illustrate the workflow's capability
in handling procedural logic and validating output correctness.
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
