window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    // get the entered language code
    const language = $('INPUT#language_code').val();
    // construct API url
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;
    $.get(url, function (greetings) {
      $('DIV#hello').text(greetings.hello);
    });
  });
};
