#!/usr/bin/node
/* imports an array and computes a new array */

const list = require('./100-data.js');
const tList = list.list;
console.log(tList);
const nList = tList.map((element, index) => element * index);
console.log(nList);
