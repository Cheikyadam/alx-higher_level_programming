#!/usr/bin/node
function max (mylist) {
  let maxi = parseInt(mylist[0]);
  let ind = 0;
  let current;
  for (let i = 0; i < mylist.length; i++) {
    current = parseInt(mylist[i]);
    if (current > maxi) {
      maxi = current;
      ind = i;
    }
  }
  return ind;
}

const list = process.argv;
if (list.length === 2) {
  console.log(0);
} else {
  if (list.length === 3) {
    console.log(0);
  } else {
    list.splice(0, 2);
    list.splice(max(list), 1);
    console.log(list[max(list)]);
  }
}
