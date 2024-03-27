#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request
  .get(url, function (error, response, body) {
    if (error) { return; }
    const rb = JSON.parse(body);
    const allchar = rb.characters;
    for (const people of allchar) {
      request
        .get(people, function (error, response, body) {
          if (error) { return; }
          const rb = JSON.parse(body);
          console.log(rb.name);
        });
    }
  });
