#!/usr/bin/node
let count = -1;
exports.logMe = function (item) {
  function help () {
    count++;
    console.log(count + ': ' + item);
  }
  help();
};
