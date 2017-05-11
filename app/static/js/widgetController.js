function playsongs(){
  $.ajax({
    url: "http://127.0.0.1:5000/envirobeatz/api/v1.0/songs", //THIS NEEDS TO CHANGE FOR PROD
    type: "GET",
    dataType: "json",
    success: function(result){

    }
  })
}

