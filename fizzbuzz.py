"""FizzBuzz implementation script."""

def fizzbuzz(start=1, end=100):
    """Generate FizzBuzz sequence from start to end inclusive."""
    result = []
    for n in range(start, end + 1):
        if n % 15 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))
    return result


def main():
    for line in fizzbuzz():
        print(line)


def test_fizzbuzz():
    expected = [
        '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
        '11', 'Fizz', '13', '14', 'FizzBuzz'
    ]
    assert fizzbuzz(1, 15) == expected


if __name__ == '__main__':
    main()
