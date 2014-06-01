$(document).ready(function () {
  $('[data-toggle=offcanvas]').click(function () {
    $('.row-offcanvas').toggleClass('active');
  });

  $('button.thumbnail').click(function(obj) {
    $(this).addClass("selected");
  });
});