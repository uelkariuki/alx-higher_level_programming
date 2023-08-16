#!/usr/bin/node

const FileSystem = require('fs');

function concat (fileA, fileB, fileC) {
  const fileData1 = FileSystem.readFileSync(fileA, 'utf8');
  const fileData2 = FileSystem.readFileSync(fileB, 'utf8');
  FileSystem.writeFileSync(fileC, fileData1 + fileData2);
}

concat('fileA', 'fileB', 'fileC');
