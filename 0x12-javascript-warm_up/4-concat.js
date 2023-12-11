#!/usr/bin/node

const argv = process.argv;
let s1 = 'undefined';
let s2 = 'undefined';
if (argv[2]) {
  s1 = argv[2];
} if (argv[3]) {
  s2 = argv[3];
}
console.log(s1 + ' is ' + s2);
