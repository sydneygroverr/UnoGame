from flask import Flask, render_template
from logic.card import Card
from logic.play import Play
from logic.main import Main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
