#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const occ = parseInt(process.argv[2]);
  let toprint = '';
  for (let i = 0; i < occ; i++) {
    toprint += 'X';
  }
  for (let i = 0; i < occ; i++) {
    console.log(toprint);
  }
}
