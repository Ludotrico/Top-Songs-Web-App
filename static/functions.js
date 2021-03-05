
var audio = new Audio()

function play(songURL) {
    console.log(songURL)
    audio.pause();
    audio = new Audio(songURL);
    audio.play();
}



