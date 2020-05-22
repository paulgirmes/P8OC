function redirect() {
    var referrer = document.referrer;
    location.replace(referrer);
    alert("Ce site requiert votre acceptation pour pouvoir fonctionner correctement. Nous allons vous rediriger vers la page précédente, Merci.");
  }
if (logged =="False") {
$('#ModalScrollable').modal('show');
} else {
$('#ModalScrollable').modal('hide');
}