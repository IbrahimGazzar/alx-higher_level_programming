#!/usr/bin/node

function factor (num) {
  if (num <= 1) {
    return 1;
  }
  return num * factor(num - 1);
}
const argv = process.argv;
let num = NaN;
let fact = 1;
if (argv[2]) {
  num = parseInt(argv[2]);
  fact = factor(num);
}
console.log(fact);
