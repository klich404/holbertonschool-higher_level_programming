/*
fetches the character name from this URL:
https://swapi-api.hbtn.io/api/people/5/?format=json
*/

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (data, textStatus) {
  data.results.map((movie) => $('UL#list_movies').append('<li>' + movie.title + '</li>'));
});
