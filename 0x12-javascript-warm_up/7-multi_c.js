#!/usr/bin/node
/* script that prints x times “C is fun” */

if (isNaN(process.argv[2]) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('C is fun');
  }
}
