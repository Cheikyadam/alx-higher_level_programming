#!/usr/bin/node
const list = require('./100-data.js');
const listIn = list.list;
console.log(listIn);
const map1 = listIn.map((x, index) => { return x * index; });
console.log(map1);
