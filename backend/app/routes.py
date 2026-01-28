from flask import Blueprint, render_template, request, jsonify, session

from .game.state import get_initial_state, check_winner

bp = Blueprint("main", __name__)


def _get_state():
    state = session.get("state")
    if not state:
        state = get_initial_state()
        session["state"] = state
    return state


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/state")
def state():
    return jsonify(_get_state())


@bp.route("/move", methods=["POST"])
def move():
    state = _get_state()
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


@bp.route("/reset", methods=["POST"])
def reset():
    state = get_initial_state()
    session["state"] = state
    return jsonify(state)

