#!/usr/bin/node

const argv = process.argv;

const FirstArg = argv[2];

const FirstArgInt = parseInt(FirstArg);

if (Number.isInteger(FirstArgInt)) {
  console.log(`My number: ${FirstArgInt}`);
} else {
  console.log('Not a number');
}
