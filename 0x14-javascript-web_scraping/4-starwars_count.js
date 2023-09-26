#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
