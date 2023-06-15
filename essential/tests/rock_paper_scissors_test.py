import pytest
import builtins
from src.rock_paper_scissors import Move, winner, get_player_move, announce_winner, playRound, startGame


@pytest.mark.parametrize('inputs, expected', [
    ([Move.ROCK , Move.ROCK], 0),
    ([Move.ROCK , Move.SCISSORS], 1),
    ([Move.PAPER , Move.ROCK], 1),
    ([Move.SCISSORS , Move.PAPER], 1),
    ([Move.SCISSORS , Move.ROCK], 2),
    ([Move.ROCK , Move.PAPER], 2),
    ([Move.PAPER , Move.SCISSORS], 2),
])
def test_valid_hexadecimal(inputs, expected):
    res = winner(inputs[0] , inputs[1] )
    assert res == expected

def test_get_player_move_valid_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'rock')
    expected = Move.ROCK
    result = get_player_move()
    assert result == expected

def test_get_player_move_valid_choice_case_insensitive(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'PaPEr')
    expected = Move.PAPER
    result = get_player_move()
    assert result == expected

def test_get_player_move_invalid_choice_then_valid_choice(monkeypatch):
    inputs = ["Invalid", "ROck"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    expected = Move.ROCK
    result = get_player_move()
    assert result == expected

def test_announce_winner(capsys):
    win_res = 1
    expected_output = "Player 1 wins, congratulations! \n\n"
    announce_winner(win_res)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_playRound(monkeypatch, capsys):
    monkeypatch.setattr("src.rock_paper_scissors.get_player_move", lambda: Move.PAPER)
    monkeypatch.setattr("src.rock_paper_scissors.random.choice", lambda x: Move.ROCK)

    playRound()
    captured = capsys.readouterr()

    assert captured.out == "PAPER vs ROCK. Who's the winner?\nPlayer 1 wins, congratulations! \n\n"