#!/usr/bin/node

const argv = process.argv;
const LenArray = 2;
const NewArray = [undefined, undefined];
for (let i = 0; i < LenArray; i++) {
  NewArray[i] = argv[i + 2];
}
const JoinedArgs = NewArray.map(String).join(' is ');
console.log(JoinedArgs);
