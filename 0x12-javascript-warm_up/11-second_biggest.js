#!/usr/bin/node

const argv = process.argv;
const nums = [];
let max = 0;
let secondmax = 0;
if (argv.length > 3) {
  for (let i = 2; i < argv.length; i++) {
    nums.push(parseInt(argv[i]));
  } max = nums[0];
  secondmax = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > max) {
      secondmax = max;
      max = nums[i];
    }
  }
} console.log(secondmax);
