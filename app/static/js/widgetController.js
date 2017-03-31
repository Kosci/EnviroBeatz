function playsongs(){
  $.ajax({
    url: "http://127.0.0.1:5000/envirobeatz/api/v1.0/songs", //THIS NEEDS TO CHANGE FOR PROD
    type: "GET",
    dataType: "json",
    success: function(result){
      ToneDenReady = window.ToneDenReady || [];
      ToneDenReady.push(function() {
          // Modify the dom and urls parameters to position
          // your player and select tracks/sets/artists to play.
          ToneDen.configure({
              soundcloudConsumerKey: 'b7966d22e02437e5d5dcce50cd95ce8d'
          });
          ToneDen.player.create({
            dom: '#player',
            urls: result.songs,
            single: false,
            skin: 'dark',
            visualizerType: 'bars',
            keyboardEvents: true
          });
      });
    }
  })
}

$(function(){
  var script = document.createElement("script");

  script.type = "text/javascript";
  script.async = true;
  script.src = "//sd.toneden.io/production/v2/toneden.loader.js";

  var entry = document.getElementsByTagName("script")[0];
  entry.parentNode.insertBefore(script, entry);
  playsongs();
  $(".tdicon-td_logo").remove();
}());
