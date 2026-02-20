 let lst = document.querySelectorAll('video')
 index = 0
 min_index = 0
 min = 0
 lst.forEach(v=>{
    if(v.duration && v.duration < min){
        min = v.duration
        min_index = index
    }
    index++
 })
 let v = lst[min_index]
 document.addEventListener('keypress', (e)=>{
    if(e.key=='s'){
        v.playbackRate=15; 
        v.play()
        v.volume = 0
    }
    else if(e.key=='p'){
        v.playbackRate=1; 
        v.play()
        v.volume = 1
    }
    console.log(e)
});