#!/usr/bin/node

const request = require('request');
request
  .get(process.argv[2], function (error, response, body) {
    if (error) { return; }
    const rb = JSON.parse(body);
    const users = [];
    for (const user of rb) {
      if (!users.includes(user.userId)) { users.push(user.userId); }
    }
    const res = {};
    for (const id of users) {
      let completed = 0;
      for (const task of rb) {
        if (task.userId === id && task.completed === true) {
          completed += 1;
        }
      }
      if (completed !== 0) { res[id] = completed; }
    }
    console.log(res);
  });
