#!/usr/bin/node

const argv = process.argv;
let size = NaN;
if (argv[2]) {
  size = parseInt(argv[2]);
  if (size) {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line = line + 'X';
      }
      console.log(line);
    }
  }
} if (!size) {
  console.log('Missing size');
}
