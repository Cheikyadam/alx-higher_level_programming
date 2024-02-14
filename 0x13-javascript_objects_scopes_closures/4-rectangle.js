#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let w = '';
    for (let i = 0; i < this.width; i++) {
      w = w + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(w);
    }
  }

  rotate () {
    const help = this.width;
    this.width = this.height;
    this.height = help;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
