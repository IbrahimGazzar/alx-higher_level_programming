#!/usr/bin/node

let counter = 0;
exports.logMe = function (item) {
  let log = '';
  log = log + counter + ': ' + item;
  counter += 1;
  console.log(log);
};
