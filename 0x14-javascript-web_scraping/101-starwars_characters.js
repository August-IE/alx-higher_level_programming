#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharacters(characters, 0);
  } else {
    console.error('Error fetching movie data:', error);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return; // Stop recursion when characters list is exhausted
  }

  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacters(characters, index + 1); // Move to the next character
    } else {
      console.error('Error fetching character data:', error);
    }
  });
}
