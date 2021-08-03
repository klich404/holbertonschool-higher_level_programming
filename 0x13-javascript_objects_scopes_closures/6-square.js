#!/usr/bin/node
/*  a class Square that defines a square
and inherits from Square of 5-square.js */

class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let x = 0; x < this.width; x++) {
      if (!c) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
