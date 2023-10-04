
window.onload = function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (greetings) {
    $('DIV#hello').text(greetings.hello);
  });
};
