#!/usr/bin/node

const argv = process.argv;
const SizeSquare = parseInt(argv[2]);

if (Number.isInteger(SizeSquare)) {
  for (let i = 0; i < SizeSquare; i++) {
    let row = '';
    for (let j = 0; j < SizeSquare; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
