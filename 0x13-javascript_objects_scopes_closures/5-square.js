#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Rectangle;
module.exports = Square;
