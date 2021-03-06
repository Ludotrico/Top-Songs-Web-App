var audio = new Audio()
var currentSongURL = null

function play(songURL) {
    console.log(songURL)
    audio.pause();


    const button = document.getElementById(songURL)

    if (currentSongURL == songURL) {
        currentSongURL = null
        button.textContent = "Play"

        button.classList.remove("btn-danger")
        button.classList.add("btn-primary")
    } else {
        audio = new Audio(songURL);
        audio.play();

        if (currentSongURL) {
            const lastButton = document.getElementById(currentSongURL)
            lastButton.textContent = "Play"


             lastButton.classList.remove("btn-danger")
             lastButton.classList.add("btn-primary")

        }

        button.textContent = "Stop"
        button.classList.remove("btn-primary")
        button.classList.add("btn-danger")

        currentSongURL = songURL

    }


}



