#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const StringToWrite = process.argv[3];

fs.writeFile(filename, StringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
