#!/usr/bin/node
/* Write a script that display the status code of a GET request. */

const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) return console.log('code: ', error);

  console.log('code: %d', response.statusCode);
});
