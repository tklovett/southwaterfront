$(document).ready(function () {
  $('#resident_info').on('submit', function(e){
        // e.preventDefault();
        $(this).append($('#stores').children());
    });
});
