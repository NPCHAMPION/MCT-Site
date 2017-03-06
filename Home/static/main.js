$(function() {
  console.log("javascript!")


  // event handler
  $("#btn-click").click(function() {
  	if ($('input').val() !== '') {
      // get input value after submit
  		var input = $('input').val()
  		console.log(input)
      $('ol').append('<li><a href="">x</a> - ' + input + '</li>');
  	}
    $('input').val('');
  });
});

// on document click of a link ('a')
$(document).on('click', 'a', function(event){
  //prevent default action - following link
  event.preventDefault();
  // remove parent element of this link ('a')
  // "this" refers to the current object
  $(this).parent().remove();
});
