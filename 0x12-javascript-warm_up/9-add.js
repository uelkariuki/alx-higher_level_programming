#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const argv = process.argv;

const addResult = add(parseInt(argv[2]), parseInt(argv[3]));

console.log(addResult);
