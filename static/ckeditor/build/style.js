
var list_field = ["book", "alem"];
for (let i = 0; i < list_field.length; i++) {
  ClassicEditor.create( document.querySelector( '#'+list_field[i] ),{
      toolbar: [ 'bulletedList' ],
  } );
}


var field = ["about-job", "about-business", "others-education", "dini-qualification", "porda", "brother_info", "sister_info", "family_details", "why_divorced", "about_weakness", "about_mehnot", "aboutme", "about_married", "partner_more_info", "address"];
for (let i = 0; i < field.length; i++) {
  ClassicEditor.create( document.querySelector( '#'+field[i] ));
}

ClassicEditor.create( document.querySelector( '#success-post' ));
ClassicEditor.create( document.querySelector( '#update-post' ));