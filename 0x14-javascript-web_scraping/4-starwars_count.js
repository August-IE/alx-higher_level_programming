#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    const wedgeMoviesCount = movies.reduce((count, movie) => {
      return movie.characters.some(character => character.endsWith('/18/')) ? count + 1 : count;
    }, 0);
    console.log(wedgeMoviesCount);
  } else {
    console.error(error);
  }
});
