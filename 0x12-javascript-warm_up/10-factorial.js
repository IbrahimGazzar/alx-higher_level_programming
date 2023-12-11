#!/usr/bin/node

const argv = process.argv;
let num = NaN;
let fact = 1;
if (argv[2]) {
  num = parseInt(argv[2]);
  while (num > 0) {
    fact *= num;
    num -= 1;
  }
}
console.log(fact);
