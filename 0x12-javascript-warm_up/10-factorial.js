#!/usr/bin/node
/* script that computes and prints a factorial */

function factorial (a) {
  if (!a) {
    return (1);
  } else {
    return(a * factorial(a - 1));
  }
}

console.log(factorial(parseInt(process.argv[2])))
