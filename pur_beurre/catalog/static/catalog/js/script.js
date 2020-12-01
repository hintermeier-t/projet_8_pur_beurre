var modification = false;
var nutriscore = document.getElementsByClassName('nutriscoreIcon');
var each;
for (each of nutriscore) {
    switch (each.innerHTML){
        case 'A':
            each.setAttribute('style','background-color:green;border-radius:50%');
            break;
        case 'B':
          each.setAttribute('style','background-color:greenyellow;border-radius:50%');
          break;
        case 'C':
          each.setAttribute('style','background-color:yellow;border-radius:50%');
          break;
        case 'D':
          each.setAttribute('style','background-color:orange;border-radius:50%');
          break;
        default:
          each.setAttribute('style','background-color:red;border-radius:50%');
    }
}

function save(clicked, url){
  //Function that call 'save' view
  $.ajax({
    type: "GET",
    url: url,
    data: {
        "product": clicked,
    },
    dataType: "json",
    success: function (data) {
        // any process in data
        alert("successfull")
    },
    failure: function () {
        alert("failure");
    }
});
}

function mailModifier(url){
  if (modification == false){
    var p = document.getElementById("modifier");
    var modificateur = document.createRange().createContextualFragment('<input id="mail" type="text" placeholder="Entrez votre adresse mail"></input><button onclick="mailSave(\'../mail_save\')">Enregistrer</button>');
    p.append(modificateur);
    modification = true;
  }
  
}

function mailSave(url){
  console.log('Appel 2');
  var mail = document.getElementById('mail')
  $.ajax({
    type: "GET",
    url: url,
    data: {
        "email": mail.value,
    },
    dataType: "json",
    success: function (data) {
        // any process in data
        alert("successfull")
    },
    failure: function () {
        alert("failure");
    }
});
  alert('Votre email est sauvegardé');
}