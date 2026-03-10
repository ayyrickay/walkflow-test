const fizzBuzz = require('./fizzbuzz');

describe('FizzBuzz function', () => {
  test.each([
    [1, '1'],
    [2, '2'],
    [3, 'Fizz'],
    [4, '4'],
    [5, 'Buzz'],
    [6, 'Fizz'],
    [10, 'Buzz'],
    [15, 'FizzBuzz'],
    [30, 'FizzBuzz'],
    [97, '97'],
    [100, 'Buzz']
  ])('fizzBuzz(%i) should return %s', (input, expected) => {
    expect(fizzBuzz(input)).toBe(expected);
  });

  test('fizzBuzz returns correct values for numbers 1 to 100', () => {
    for (let i = 1; i <= 100; i++) {
      let expected = '';
      if (i % 3 === 0) expected += 'Fizz';
      if (i % 5 === 0) expected += 'Buzz';
      if (expected === '') expected = i.toString();
      expect(fizzBuzz(i)).toBe(expected);
    }
  });
});
