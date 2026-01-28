from flask import Flask, render_template, request, jsonify, session
import os

from dotenv import load_dotenv

load_dotenv()  # load variables from .env

app = Flask(__name__)
app.secret_key = os.getenv("app.secret_key", "change-this-secret")  # needed for sessions


def get_initial_state():
    return {
        "board": [None] * 9,
        "current_player": "X",
        "game_over": False,
        "winner": None,
        "message": "Player X's turn",
    }


def check_winner(board, player):
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)


def get_state():
    state = session.get("state")
    if not state:
        state = get_initial_state()
        session["state"] = state
    return state


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/state")
def state():
    return jsonify(get_state())


@app.route("/move", methods=["POST"])
def move():
    state = get_state()
    if state["game_over"]:
        return jsonify(state)

    data = request.get_json()
    index = data.get("index")

    # Validate move
    if index is None or not (0 <= index < 9) or state["board"][index] is not None:
        state["message"] = "Invalid move. Try another cell."
        session["state"] = state
        return jsonify(state)

    player = state["current_player"]
    state["board"][index] = player

    if check_winner(state["board"], player):
        state["game_over"] = True
        state["winner"] = player
        state["message"] = f"Player {player} wins!"
    elif all(cell is not None for cell in state["board"]):
        state["game_over"] = True
        state["winner"] = None
        state["message"] = "It's a draw!"
    else:
        state["current_player"] = "O" if player == "X" else "X"
        state["message"] = f"Player {state['current_player']}'s turn"

    session["state"] = state
    return jsonify(state)


@app.route("/reset", methods=["POST"])
def reset():
    state = get_initial_state()
    session["state"] = state
    return jsonify(state)


if __name__ == "__main__":
    app.run(debug=True)

