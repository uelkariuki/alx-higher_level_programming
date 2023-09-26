#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, data) => {
  if (error) {
    return console.log(error);
  }
  const tasksCompleted = data.body.reduce((accumulator, task) => {
    if (task.completed) {
      if (accumulator[task.userId]) {
        accumulator[task.userId]++;
      } else {
        accumulator[task.userId] = 1;
      }
    }
    return accumulator;
  }, {});
  console.log(tasksCompleted);
});
