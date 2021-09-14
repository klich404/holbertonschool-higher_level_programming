#!/usr/bin/node
/* Write a script that display the status code of a GET request. */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films';
request(url, function (error, response, body) {
  if (error) return console.log('code: ', error);
  const results = JSON.parse(body).results[0];
  const characters = results.characters;
  for (const character of characters) {
    if (character.endsWith('18/') === true) {
      request(character, function (error, response, body) {
        if (error) return console.log('code: ', error);
        const films = JSON.parse(body).films;
        console.log(films.length);
      });
    }
  }
});
