#!/usr/bin/node
let first = 'undefined ';
const second = 'is ';
let third = 'undefined';
if (process.argv.length >= 3) {
  first = process.argv[2] + ' ';
}
if (process.argv.length >= 4) {
  third = process.argv[3];
}
console.log(first + second + third);
