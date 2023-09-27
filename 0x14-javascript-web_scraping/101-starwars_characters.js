#!/usr/bin/node

const request = require('request');
const util = require('util');
// converts callback-based "request" to return Promises
const get = util.promisify(request.get);
const movieId = process.argv[2];
const apiEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

get(apiEndpoint, { json: true }).then(async (response) => {
  const urlCharacters = response.body.characters;
  const characterPromises = urlCharacters.map(url => get(url, { json: true }));
  const characterResponses = await Promise.all(characterPromises);

  characterResponses.forEach((resp) => {
    console.log(resp.body.name);
  });
}).catch((error) => {
  console.log(error);
});
