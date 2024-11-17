#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Base URL for the Star Wars API
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

// Fetch the movie data
request(`${baseUrl}${movieId}/`, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${res.statusMessage}`);
    process.exit(1);
  }

  // Parse the movie data
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to fetch and print character names in order
  const fetchCharacterName = (url, callback) => {
    request(url, (err, res, body) => {
      if (err) return callback(err);
      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  };

  // Iterate over characters and fetch their names
  const characterPromises = characters.map(
    (url) =>
      new Promise((resolve, reject) => {
        fetchCharacterName(url, (err, name) => {
          if (err) reject(err);
          else resolve(name);
        });
      })
  );

  // Wait for all character names and print them
  Promise.all(characterPromises)
    .then((names) => names.forEach((name) => console.log(name)))
    .catch((err) => console.error(err));
});

