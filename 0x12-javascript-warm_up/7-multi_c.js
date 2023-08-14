#!/usr/bin/node

const argv = process.argv;

const string = 'C is fun';

const FirstArg = parseInt(argv[2]);

for (let i = 0; i < FirstArg; i++) {
  console.log(string);
}
