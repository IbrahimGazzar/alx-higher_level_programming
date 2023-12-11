#!/usr/bin/node

const argv = process.argv;
let integer;
if (argv[2]) {
  integer = parseInt(argv[2]);
  if (integer) {
    console.log('My number: ' + integer);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
