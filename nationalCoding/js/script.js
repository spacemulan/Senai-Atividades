const vid = document.getElementById('video');
const btn = document.getElementById('btn');
function myFunction(){
    if (vid.paused){
            vid.play();
            btn.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i> Pause';
    }
    else{
        vid.pause();
        btn.innerHTML='<i class="fa fa-play" aria-hidden="true"></i> Play';
    }
}