#!/usr/bin/node
/* script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer */

if (isNaN(process.argv[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
