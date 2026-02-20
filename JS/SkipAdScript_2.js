 
 let v = document.querySelector('video')
 document.addEventListener('keypress', (e)=>{
    if(e.key=='s'){
        v.playbackRate=15; 
        v.play()
    }
    else if(e.key=='p'){
        v.playbackRate=1; 
        v.play()
    }
    console.log(e)
});