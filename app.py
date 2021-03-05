from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)



songs = ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3"]
ACCESS_TOKEN = None


@app.route("/")
@app.route("/globalTop50")
def home():
    getSpotifyToken()

    return render_template("home.html", songs=getTopSongs("37i9dQZEVXbMDoHDwVN2tF"))


@app.route("/USATop50")
def USATop50():
    getSpotifyToken()

    return render_template("home.html", songs=getTopSongs("37i9dQZEVXbLp5XoPON0wI"))

@app.route("/canadaTop50")
def canadaTop50():
    getSpotifyToken()

    return render_template("home.html", songs=getTopSongs("37i9dQZEVXbKj23U1GF4IR"))

@app.route("/mexicoTop50")
def mexicoTop50():
    getSpotifyToken()

    return render_template("home.html", songs=getTopSongs("37i9dQZEVXbO3qyFxbkOE1"))



def getSpotifyToken():
    global ACCESS_TOKEN
    url = "https://accounts.spotify.com/api/token"

    payload = 'grant_type=client_credentials'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'Accept': '*/*',
        'Authorization': 'Basic MDYyMjY0MGFmMzczNDc2MGE5N2JmMjU5N2FkNmQ3YmQ6NjFjOGIyNjI0NjE2NDhkZGI0MDY0NTgyZjNmMWQ0MTY=',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__Host-device_id=AQCft2pVMNCQ57d2DX2BzAicoXajVnGC6QvoRKEcAcRsAgeJCK135kg8zje_8mNnGF5H-_bGxJEqCNicsnIcMvOs5MuwHKwcdJg; _ga=GA1.2.1982453259.1600384441; sp_dc=AQAabGC9zpIwUSEe20uLNGAKwlaYnKYuYRodwB7PHcT1qAKwTyZ34wPNuc0v1ejVWBrvIqqO8wLS1zEt8-S_6a6SPPEfemNt9gIWbaEyLw; sp_key=cf86ab78-0129-4d64-a2ae-6cf948921c68'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    responseObj = response.json()
    ACCESS_TOKEN = responseObj['access_token']


def getTopSongs(id):
    url = f"https://api.spotify.com/v1/playlists/{id}"

    payload = {}
    headers = {
        'Accept': '*/*',
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Cookie': '_ga=GA1.2.1982453259.1600384441; sp_dc=AQAabGC9zpIwUSEe20uLNGAKwlaYnKYuYRodwB7PHcT1qAKwTyZ34wPNuc0v1ejVWBrvIqqO8wLS1zEt8-S_6a6SPPEfemNt9gIWbaEyLw; sp_key=cf86ab78-0129-4d64-a2ae-6cf948921c68'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    obj = response.json()
    songs = []
    for item in obj['tracks']['items']:
        song = item['track']
        artists = song['artists']
        image = song['album']['images'][0]['url']
        artistNames = ""
        for artist in artists:
            artistNames += artist['name'] + ', '
        artistNames = artistNames[:-2]
        songs.append({"songName": song['name'], "artists": artistNames, "mp3": song['preview_url'], "image": image})
    print(songs)

    return songs





if __name__ == "__main__":
    app.run(debug=True)