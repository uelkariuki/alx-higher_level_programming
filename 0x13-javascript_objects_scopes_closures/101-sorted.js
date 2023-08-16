#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedOccur = {};

for (const [userId, Occur] of Object.entries(dict)) {
  if (!sortedOccur[Occur]) {
    sortedOccur[Occur] = [];
  }
  sortedOccur[Occur].push(userId);
}

console.log(sortedOccur);
