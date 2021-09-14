#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file*/

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) return console.log('code: ', error);
  fs.writeFile(process.argv[3], body, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
});
