#!/usr/bin/node
/* Write a script that display the status code of a GET request. */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) return console.log('code: ', error);
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, function (error, response, body) {
      if (error) return console.log('code: ', error);
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
