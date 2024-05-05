$(document).ready(function () {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
        console.log(data.results);
        $.each(data.results, function (i, film) {
            $('#list_movies').append('<li>' + film.title + '</li>');
        });
    });
});