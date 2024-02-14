#!/usr/bin/node
exports.converter = function (base) {
  return function conv (n) {
    return n.toString(base);
  };
};
