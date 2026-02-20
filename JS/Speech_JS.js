function speak(txt){
    let utterance = new SpeechSynthesisUtterance(txt);
    const voices = speechSynthesis.getVoices();
    utterance.voice = voices[6]; 
    speechSynthesis.speak(utterance).
}

var stop_speech = false;
let paras = document.querySelectorAll('p')
for(let i=0; i<paras.length; ++i){
    if(stop_speech){
        break;
    }
    paras[i].style.backgroundColor = 'yellow';
    speak(paras[i].innerText);
}

function stop(){
    stop_speech = true;
}