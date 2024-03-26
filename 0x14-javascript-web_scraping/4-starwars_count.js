#!/usr/bin/node

const request = require('request');
request
  .get(process.argv[2], function (error, response, body) {
    if (error) { return; }
    const rb = JSON.parse(body);
    let count = 0;
    const results = rb.results;
    for (const el of results) {
      const charract = el.characters;
      for (const url of charract) {
        if (url.includes('18')) { count += 1; }
      }
    }
    console.log(count);
  });
