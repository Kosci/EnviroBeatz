var src = "https://w.soundcloud.com/player/?url=";
var srcEnd = "&auto_play=falsehide_related=falseshow_comments=trueshow_user=trueshow_reposts=falsevisual=true";

function playsongs(){
  var csrf_token = "{{ csrf_token() }}";
  $.ajax({
    beforeSend: function(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("Access-Control-Allow-Origin", csrf_token);
      }
    },
    url: "http://localhost:5000/envirobeatz/api/v1.0/songs/random",
    type: "GET",
    dataType: "json",
    success: function(result){
      $("#songPlayer").attr("src", src + result + srcEnd);
      console.log("refreshed");
    }
  })
}

$(document).ready(function(){
  setInterval(playsongs, 10000);
  // playsongs();
});

