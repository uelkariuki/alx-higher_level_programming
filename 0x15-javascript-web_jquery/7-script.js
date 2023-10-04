$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      $('#character').append('<div id="character">' + data.name + '</div>');
    }
  });
});
