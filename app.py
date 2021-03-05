from flask import Flask, render_template, url_for

app = Flask(__name__)



songs = ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"]

@app.route("/")
def home():
    return render_template("home.html", songs=songs)



if __name__ == "__main__":
    app.run(debug=True)