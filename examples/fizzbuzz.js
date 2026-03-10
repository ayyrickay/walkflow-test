// FizzBuzz example in JavaScript
// Prints numbers from 1 to 100
// For multiples of 3, prints "Fizz"
// For multiples of 5, prints "Buzz"
// For multiples of both 3 and 5, prints "FizzBuzz"

for (let i = 1; i <= 100; i++) {
  let output = '';
  if (i % 3 === 0) output += 'Fizz';
  if (i % 5 === 0) output += 'Buzz';
  console.log(output || i);
}
