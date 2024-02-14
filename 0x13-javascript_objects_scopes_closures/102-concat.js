#!/usr/bin/node
const fs = require('fs');
function concatFiles (fileA, fileB, fileC) {
  try {
    const contA = fs.readFileSync(fileA, 'utf-8');
    const contB = fs.readFileSync(fileB, 'utf-8');
    const contC = contA + contB;
    fs.writeFileSync(fileC, contC);
  } catch (e) {}
}
if (process.argv.length === 5) {
  concatFiles(process.argv[2], process.argv[3], process.argv[4]);
}
