#!/usr/bin/node
const inDict = require('./101-data.js');
const dictIn = inDict.dict;
const values = Object.values(dictIn);
const valueUn = [];
let j = 0;
for (let i = 0; i < values.length; i++) {
  if (!valueUn.includes(values[i])) {
    valueUn[j] = values[i];
    j++;
  }
}
const newDic = {};
for (let i = 0; i < valueUn.length; i++) {
  let j = 0;
  const list = [];
  Object.entries(dictIn).forEach(function ([cle, valeur]) {
    if (dictIn[cle] === valueUn[i]) {
      list[j] = cle;
      j++;
    }
  });
  newDic[valueUn[i]] = list;
}
console.log(newDic);
