function playsongs(){
  var widget = SC.Widget('sc-widget');
  $.ajax({
    url: "http://127.0.0.1:5000/envirobeatz/api/v1.0/songs", //THIS NEEDS TO CHANGE FOR PROD
    type: "GET",
    dataType: "json",
    success: function(result){
      widget.bind(SC.Widget.Events.READY, function(){
        widget.load("https%3A//api.soundcloud.com/tracks/" + result.songs[1].id, {auto_play: false});
      });
    }
  })
}

$(function(){
      var widget = SC.Widget('sc-widget');
      playsongs();
}());
