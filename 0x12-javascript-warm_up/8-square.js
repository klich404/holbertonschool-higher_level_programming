#!/usr/bin/node
/* script that prints a square */

if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for(let x = 0; x < process.argv[2]; x++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
