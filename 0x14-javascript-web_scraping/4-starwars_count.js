#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18';

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const films = data.films;
    console.log(films.length);
  }
});
