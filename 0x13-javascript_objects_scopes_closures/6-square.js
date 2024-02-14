#!/usr/bin/node
const Square2 = require('./5-square');
class Square extends Square2 {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let w = '';
      for (let i = 0; i < this.height; i++) {
        w = w + c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(w);
      }
    }
  }
}
module.exports = Square;
