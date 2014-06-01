$(document).ready(function () {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });

  $('button.thumbnail').click(function() {
    if ($(this).hasClass("selected")) {
      $(this).removeClass("selected");
      $(this).blur()
    } else {
      $(this).addClass("selected");
    }
  });

  $('[data-save]').click(function() {
    store_string = ""
    $('button.thumbnail.selected').each(function() {
      store_string += $(this).attr("value") + ",";
    });
    console.log(store_string)
    window.location = "/resident/?stores=" + store_string;
  })
});