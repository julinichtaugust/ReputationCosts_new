
errors = document.getElementsByClassName("otree-form-errors alert alert-danger").item(0)
if (errors != null) {
    errors.innerHTML="Mindestens eine Frage wurde nicht beantwortet. Bitte überprüfen Sie Ihre Antwort(en)! "
}else{
    console.log(errors)
}
