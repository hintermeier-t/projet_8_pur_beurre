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
  console.log(url);
  console.log(clicked);
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
