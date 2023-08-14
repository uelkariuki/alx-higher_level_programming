#!/usr/bin/node

const argv = process.argv;

const result = argv.slice(2);

if (!result.some(() => true)) {
  console.log('No argument');
} else {
  result.forEach((value, index) => {
    console.log(`${value}`);
  });
}
