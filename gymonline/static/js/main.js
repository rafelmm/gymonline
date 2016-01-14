

$(document).ready(function(){
	// Language form in the navbar of the base.html template
	$('.set_language-flag').click(function(){
		idioma = $(this).attr('id');
		if ( idioma == 'set_language-esp'){
			$("#set_language_select").val("es");
		} else if ( idioma == 'set_language-cat'){
			$("#set_language_select").val("ca");
		} else {
			$("#set_language_select").val("en");
		}
		$("#set_language_form").submit();
	});
			
});