## Tic Tac Toe Web App (Flask + Frontend)

This repository contains a simple **Tic Tac Toe** game built with:

- **Backend**: Python + Flask
- **Frontend**: Plain HTML, CSS, and JavaScript
- **Structure**: Mono-repo style with clear `backend` and `frontend` modules

The game runs in the browser, while all game state (board, current player, winner) is managed on the Flask backend.

---

### Repository structure

```text
TicTacToe/
├── backend/
│   ├── __init__.py            # Backend package marker
│   └── app/
│       ├── __init__.py        # Flask app factory (create_app)
│       ├── routes.py          # API and page routes (/, /state, /move, /reset)
│       └── game/
│           ├── __init__.py
│           └── state.py       # Pure game logic (initial state, winner check)
│
├── frontend/
│   ├── templates/
│   │   └── index.html         # Main HTML page, loads CSS/JS via url_for
│   └── static/
│       ├── css/
│       │   └── style.css      # Page styling
│       └── js/
│           └── app.js         # Frontend game logic and API calls
│
├── main.py                    # Entry point, creates app and runs server
├── .env                       # Environment variables (secret key, etc.) – ignored by git
├── .gitignore                 # Ignore rules for Python, env, editor files, etc.
```

---

### How it works

- The **frontend** (`frontend/templates/index.html` + `frontend/static/...`) renders the board and handles user interactions (clicks, reset).
- The **backend** exposes JSON endpoints:
  - `GET /state` – returns current board, current player, game_over, message.
  - `POST /move` – accepts `{ "index": 0-8 }`, applies the move, returns new state.
  - `POST /reset` – resets game state and returns the new state.
- Game state is stored in the Flask **session**, so each browser session gets its own game.

---

### Requirements

- Python 3.8+ (recommended)

Install dependencies:

```bash
pip install flask python-dotenv
```

---

### Environment configuration

Create a `.env` file in the project root:

```env
app.secret_key="your-secret-key-here"
```

This value is loaded in `backend/app/__init__.py` using `python-dotenv` and used as the Flask `secret_key`.  
The `.env` file is listed in `.gitignore`, so it will **not** be committed.

---

### Running the app locally

From the project root:

```bash
python main.py
```

The app is configured to run on port **5001**:

```text
http://127.0.0.1:5001/
```

Open that URL in your browser to play:

- Click any square to place `X` or `O`.
- The status text shows whose turn it is, or who won / if it’s a draw.
- Click **Reset Game** to start a new round.

---

### Notes on structure (for AI / Cursor use)

- **Backend code** lives under `backend/app` (Flask app, routes, and game logic).
- **Frontend code** lives under `frontend` (templates and static assets).
- `main.py` is a thin entrypoint that imports `create_app` from `backend.app` and runs it.

This layout is designed to be easy for both humans and AI tools (like Cursor) to navigate:  
backend vs frontend, routes vs game functions, and entrypoint vs modules are clearly separated.


