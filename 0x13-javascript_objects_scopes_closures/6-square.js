#!/usr/bin/node
/*  a class Square that defines a square
and inherits from Square of 5-square.js */

class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let x = 0; x < this.size; x++) {
      if (!c) {
        console.log('X'.repeat(this.size));
      } else {
        console.log('C'.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
