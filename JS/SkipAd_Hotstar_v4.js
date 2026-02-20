let i = setInterval(() => {
    let v_arr = document.querySelectorAll('video')
    if (v_arr.length > 1) {
        v_arr[0].playbackRate = 15
        v_arr[0].volume = 0
    }
    else if (v_arr.length == 1) {
        v_arr[0].playbackRate = 1
        v_arr[0].volume = 1
    }
}, 1000);