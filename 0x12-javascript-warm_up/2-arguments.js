#!/usr/bin/node
/* script that prints a message depending of the number of arguments passed */

if (!console.log.arguments) {
  console.log('No argument');
} else if (console.log.arguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
