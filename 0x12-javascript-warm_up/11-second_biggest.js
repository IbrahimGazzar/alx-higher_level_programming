#!/usr/bin/node

const argv = process.argv;
const nums = [];
let max = -999999;
let secondmax = -999999;
if (argv.length > 3) {
  for (let i = 2; i < argv.length; i++) {
    nums.push(parseInt(argv[i]));
  } for (let i = 0; i < nums.length; i++) {
    if (nums[i] > max) {
      secondmax = max;
      max = nums[i];
    } else if (nums[i] > secondmax && nums[i] < max) {
      secondmax = nums[i];
    }
  }
} else {
  secondmax = 0;
} console.log(secondmax);
