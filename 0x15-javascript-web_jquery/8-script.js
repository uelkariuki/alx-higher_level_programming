$(function () {
  const $listMovies = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (filmsData) {
      $.each(filmsData.results, function (i, filmTitles) {
        $listMovies.append('<li>' + filmTitles.title + '</li>');
      });
    }
  });
});
