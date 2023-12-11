#!/usr/bin/node

const argv = process.argv;
let num = NaN;
if (argv[2]) {
  num = parseInt(argv[2]);
  if (num || num === 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
} if (!num) {
  console.log('Missing number of occurrences');
}
