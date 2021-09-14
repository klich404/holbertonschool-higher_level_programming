#!/usr/bin/node
/* Write a script that display the status code of a GET request. */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) return console.log('code: ', error);
  console.log(JSON.parse(body).title);
});
