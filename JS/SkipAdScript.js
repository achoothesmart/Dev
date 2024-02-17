var timer
clearInterval(timer)
timer = setInterval(() => {
    if (document.querySelectorAll('video').length > 1) {
        document.querySelectorAll('video')[0].playbackRate = 15
        document.querySelectorAll('video')[0].volume = 0
        document.querySelectorAll('video')[0].play()
    }
}, 1000);
