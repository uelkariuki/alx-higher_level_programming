#!/usr/bin/node

const argv = process.argv.slice(2).map(Number);
const maxInt = Math.max(...argv);
const filteredArgs = argv.filter(num => num !== maxInt);

// if filteredArgs length is greater than zero, then Math.max(...filteredArgs) else return 0 to show array is empty
// ... is the spread operator
const secondmaxInt = filteredArgs.length > 0 ? Math.max(...filteredArgs) : 0;

console.log(secondmaxInt);
