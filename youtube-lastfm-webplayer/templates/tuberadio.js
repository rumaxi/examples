    var player;
 
     function onPlayerReady(event) {
         event.target.playVideo();
     }
 
     function onPlayerStateChange(event) {        
         if(event.data === 0) {            
             nextTrack()
         }
    }

    function nextTrack() {
        console.log ('next track')
             $.get ("randomvideo", function(data) {
                 console.log (data)
                player.loadVideoById(data)
             })
    }

/*    $( document ).ready(function() {

    });
*/

    function onYouTubePlayerAPIReady() 
    {
        $.get ("randomvideo", function (data) {
            player = new YT.Player ('player', 
                        {   videoId: data,
                            playerVars: { 'autoplay':'1', 'controls':'0', 'showinfo':'0', 'rel':'0', 'modestbranding':'1' },
                            events: { 'onStateChange':onPlayerStateChange, 'onReady':onPlayerReady}
                        }
                        )
        
        })

    }

