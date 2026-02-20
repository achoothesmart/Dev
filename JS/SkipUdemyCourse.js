var n = 0
try{
    clearInterval(i)
}catch(ex){}

try{
var i = setInterval(()=>{
    document.querySelector('video').currentTime = document.querySelector('video').duration
    n++;
    console.log('skipped ' + n + ' videos!')
}, 1000)
}catch(ex){
    console.log('No video file found in the page! Please navigate >>')
}
print()