<script type="text/javascript">

var name = new LiveValidation( 'id_name', {onlyOnSubmit: true } );
name.add( Validate.Presence );

var email = new LiveValidation( 'id_email', {onlyOnSubmit: true } );
email.add( Validate.Email );

var salary = new LiveValidation( 'id_salary', {onlyOnSubmit: true } );
salary.add( Validate.Numericality);

var title = new LiveValidation( 'id_title', {onlyOnSubmit: true } );
title.add( Validate.Presence );

</script>