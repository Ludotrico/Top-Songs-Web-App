var audio = new Audio()
var currentSongURL = null

function play(songURL) {
    console.log(songURL)
    audio.pause();


    const button = document.getElementById(songURL)

    if (currentSongURL == songURL) {
        currentSongURL = null
        button.textContent = "Play"
    } else {
        audio = new Audio(songURL);
        audio.play();

        if (currentSongURL) {
            const lastButton = document.getElementById(currentSongURL)
            lastButton.textContent = "Play"
        }

        button.textContent = "Pause"

        currentSongURL = songURL

    }


}



