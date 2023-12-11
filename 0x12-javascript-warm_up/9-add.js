#!/usr/bin/node

const argv = process.argv;
let num1 = NaN;
let num2 = NaN;
if (argv[2]) {
  num1 = parseInt(argv[2]);
} if (argv[3]) {
  num2 = parseInt(argv[3]);
} if ((num1 || num1 === 0) && (num2 || num2 === 0)) {
  num1 += num2;
  console.log(num1);
} else {
  console.log('NaN');
}
