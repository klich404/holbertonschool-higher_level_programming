#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments. */

function nextBiggest(arr) {
  let max = -Infinity, result = -Infinity;

  for (const value of arr) {
    const nr = Number(value)

    if (nr > max) {
      [result, max] = [max, nr] // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }

  return result;
}

if (!process.argv[2] || !process.argv[3]) {
  console.log('0');
} else {
  const arr = [];
  for (let x = 2; x < process.argv.length; x++) {
    arr.push(process.argv[x]);
  }
  console.log(nextBiggest(arr));
}
