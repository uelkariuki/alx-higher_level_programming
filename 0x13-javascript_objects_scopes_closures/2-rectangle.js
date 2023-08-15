#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w)) {
      return {};
    } else {
      this.width = w;
    }

    if (h <= 0 || !Number.isInteger(h)) {
      return {};
    } else {
      this.height = h;
    }
  }
}

module.exports = Rectangle;
