#!/usr/bin/node

const argv = process.argv;
let num;
if (argv[2]) {
  num = parseInt(argv[2]);
  if (num || num === 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
