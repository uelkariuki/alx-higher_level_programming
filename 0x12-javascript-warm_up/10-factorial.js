#!/usr/bin/node

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

const argv = process.argv;
const result = factorial(parseInt(argv[2]));
console.log(result);
