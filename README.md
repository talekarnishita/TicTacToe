# Tic Tac Toe Web App (Flask + Cursor)

This is a simple Tic Tac Toe web application built with **Python (Flask)** and created interactively using the **Cursor AI coding assistant**.

The game runs in your browser, with the game state managed on the Flask backend and a small amount of JavaScript on the frontend to communicate with the server.

---

## Features

- **Web-based Tic Tac Toe** with a clean, minimal UI.
- **Server-side game logic** using Flask and sessions.
- **Interactive frontend** that talks to the backend via JSON (`/state`, `/move`, `/reset`).
- **Secret key** loaded from a `.env` file (not committed to git).
- Project structure and many code edits were generated and refined using **Cursor**.

---

## How this was created with Cursor

1. **Initial setup**
   - Started with an empty `main.py` file in Cursor.
   - Asked Cursor to build a simple Tic Tac Toe game on a webpage using Python.
   - Cursor generated a minimal Flask app that served an HTML page via `render_template_string`.

2. **Making the page interactive and dynamic**
   - Requested that the game be "interactive and dynamic" so users could play online.
   - Cursor moved the game logic into **Flask**:
     - Introduced a server-side board, current player, and winner using Flask **sessions**.
     - Added JSON endpoints:
       - `GET /state` – returns the current game state.
       - `POST /move` – applies a move and returns the updated state.
       - `POST /reset` – resets the game.
   - Cursor updated the frontend JavaScript so it:
     - Fetches the current state from `/state`.
     - Sends moves to `/move`.
     - Resets the game via `/reset`.

3. **Extracting the HTML into a template**
   - Asked to add an `index.html` file.
   - Cursor:
     - Created `templates/index.html` and moved the HTML/JS there.
     - Updated `main.py` to use `render_template("index.html")`.

4. **Environment variables and secrets**
   - Created a `.env` file to store the Flask `secret_key`.
   - Asked Cursor to wire this into the app:
     - Added `python-dotenv` usage (`load_dotenv()`).
     - Loaded `app.secret_key` from the `.env` file instead of hardcoding it.
   - Updated `.gitignore` so `.env` is **not** committed.

5. **Git setup**
   - With Cursor's help:
     - Created a proper `.gitignore` for Python, Flask, macOS, editors, and `.env`.
     - Initialized a git repository.
     - Prepared commands to add, commit, and push the project to GitHub.

Throughout this process, Cursor was used to:
- Generate boilerplate Flask code.
- Refactor the app from inline HTML to a dedicated template.
- Add routes, JSON APIs, and session handling.
- Keep secrets out of version control.

---

## Project structure

```text
TicTacToe/
├── main.py              # Flask application with routes and game logic
├── templates/
│   └── index.html       # Frontend UI and JavaScript for Tic Tac Toe
├── .env                 # Environment variables (e.g., app.secret_key) – ignored by git
├── .gitignore           # Git ignore rules for Python, env, editor files, etc.
└── README.md            # This file
```

---

## Requirements

- Python 3.8+ (recommended)

Install dependencies:

```bash
pip install flask python-dotenv
```

---

## Configuration

Create a `.env` file in the project root (Cursor already did this during setup):

```env
app.secret_key="12345678qyerssss"
```

This secret key is used by Flask to sign session cookies.  
Because `.env` is listed in `.gitignore`, it will **not** be pushed to your git repository.

---

## Running the app

From the project root (`TicTacToe`):

```bash
python main.py
```

Then open your browser to:

```text
http://127.0.0.1:5000/
```

You’ll see the Tic Tac Toe board:
- Click cells to place X and O.
- The status text shows whose turn it is, or who won / if it’s a draw.
- Use the **Reset Game** button to start a new game.

---

## Playing with others

Because the game state is stored on the server (via Flask sessions), each browser/device maintains its own session:

- On your own machine: open multiple browser windows to test.
- On the same network: use your machine’s LAN IP instead of `127.0.0.1` and share the URL.

For true internet-wide access, you can deploy this app (e.g., to Render, Railway, or another hosting provider) and configure the environment variables there.

---

## Extending the project

Some ideas to build on this (you can ask Cursor to help with each step):

- Add a simple **scoreboard** across games.
- Add a **computer opponent (AI)** that makes basic moves.
- Add **usernames** or a lobby for multiple games.
- Improve the styling with a CSS framework like Tailwind or Bootstrap.
