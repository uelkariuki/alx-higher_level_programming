#!/usr/bin/node

const FileSystem = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fileData1 = FileSystem.readFileSync(fileA, 'utf8');
const fileData2 = FileSystem.readFileSync(fileB, 'utf8');
FileSystem.writeFileSync(fileC, fileData1 + fileData2);
