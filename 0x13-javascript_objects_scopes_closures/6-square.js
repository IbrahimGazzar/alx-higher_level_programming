#!/usr/bin/node

const squareParent = require('./5-square.js');
module.exports = class Square extends squareParent {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        if (c === undefined) {
          line = line + 'X';
        } else {
          line = line + c;
        }
      }
      console.log(line);
    }
  }
};
