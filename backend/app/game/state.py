"""
Pure game-state functions for Tic Tac Toe.
"""

from typing import List, Dict, Optional, Any


def get_initial_state() -> Dict[str, Any]:
    return {
        "board": [None] * 9,
        "current_player": "X",
        "game_over": False,
        "winner": None,
        "message": "Player X's turn",
    }


def check_winner(board: List[Optional[str]], player: str) -> bool:
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

