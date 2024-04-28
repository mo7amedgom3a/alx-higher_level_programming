#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

const character_ID = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const filme of films) {
      for (const character of filme.characters) {
        if (character.includes(character_ID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
