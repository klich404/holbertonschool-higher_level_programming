#!/usr/bin/node
/* Write a script that display the status code of a GET request. */

const request = require('request');
const url = process.argv[2];
const dictionary = {}
request(url, function (error, response, body) {
  if (error) return console.log('code: ', error);
  const ids = (JSON.parse(body));
  for (const users of ids) {
      if (users.complete === true) {
        if (dictionary[users.userId]) {
            dictionary[users.userId]
        } else {
            dictionary[users.userId] = 1
        }
      }
  }
});
