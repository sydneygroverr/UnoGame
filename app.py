from flask import Flask, render_template, jsonify
# from logic.card import Card
# from logic.play import Play
from logic.main import UnoGame

app = Flask(__name__)

# Initialize the game
game = UnoGame()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/state', methods=['GET'])
def get_state():
    return jsonify(game.get_game_state())


@app.route('/play', methods=['POST'])
def play_turn():
    result = game.playGame()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
