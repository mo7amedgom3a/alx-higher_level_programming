#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

const characterid = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const filme of films) {
      for (const character of filme.characters) {
        if (character.includes(characterid)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
