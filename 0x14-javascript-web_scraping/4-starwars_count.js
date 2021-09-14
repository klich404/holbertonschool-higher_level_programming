#!/usr/bin/node
/* Write a script that display the status code of a GET request. */

const request = require('request');
const url = process.argv[2];
let films = 0;
request(url, function (error, response, body) {
  if (error) return console.log('code: ', error);
  const results = JSON.parse(body).results;
  for (const movies of results) {
    const characters = movies.characters;
    for (const character of characters) {
      if (character.endsWith('18/') === true) {
        films = films + 1;
      }
    }
  }
  console.log(films);
});
