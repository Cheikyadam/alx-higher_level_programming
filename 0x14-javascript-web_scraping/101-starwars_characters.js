#!/usr/bin/node

async function executeRequestsSequentially (urls) {
  for (const url of urls) {
    await new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
}

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request
  .get(url, function (error, response, body) {
    if (error) { return; }
    const rb = JSON.parse(body);
    const allchar = rb.characters;
    executeRequestsSequentially(allchar);
  }
  );
