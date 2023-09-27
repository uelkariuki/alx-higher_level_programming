#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request(apiEndpoint, { json: true }, (error, response, data) => {
  if (error) {
    return console.log(error);
  }
  const urlCharacters = data.characters;
  urlCharacters.forEach(url => {
    request(url, { json: true }, (error, response, characterData) => {
      if (error) {
        return console.log(error);
      }
      console.log(characterData.name);
    });
  });
});
