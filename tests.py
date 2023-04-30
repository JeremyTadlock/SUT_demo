import pytest
from GenerateNumbers import GenerateNumbers
from ScoreBoard import ScoreBoard
import game


# test_GenerateNumbers.py

# test init def
def test_GenerateNumbers_init():
    gn = GenerateNumbers(1, 10)
    assert gn.min == 1
    assert gn.max == 10
    assert isinstance(gn.player_number, int)
    assert isinstance(gn.ai_number, int)


# test setNumbers using automatic testing
@pytest.mark.parametrize("min,max", [(1, 4), (1, 6), (1, 20)])
def test_setNumbers(min, max):
    gn = GenerateNumbers(min, max)
    number = gn.setNumbers()
    assert min <= number <= max


# test getPlayerNumber automatically
@pytest.mark.parametrize("min,max", [(1, 20), (1, 100)])
def test_getPlayerNumber(min, max):
    gn = GenerateNumbers(min, max)
    assert min <= gn.getPlayerNumber() <= max


# test getAiNumber automatically
@pytest.mark.parametrize("min,max", [(1, 20), (1, 100)])
def test_getAiNumber(min, max):
    gn = GenerateNumbers(min, max)
    assert min <= gn.getAiNumber() <= max


# test ScoreBoard.py():

# test init def
def test_ScoreBoard_init():
    sb = ScoreBoard("Jeremy", 3)
    assert sb.player_name == "Jeremy"
    assert sb.winningGoal == 3
    assert isinstance(sb.human_score, int)
    assert isinstance(sb.ai_score, int)


# test getScorePlayer
def test_getScorePlayer():
    sb = ScoreBoard("Jeremy", 3)
    ps = sb.human_score
    assert ps == sb.getScorePlayer()


# test getScoreAi
def test_getScoreAi():
    sb = ScoreBoard("Jeremy", 3)
    ais = sb.ai_score
    assert ais == sb.getScoreAi()


# test addScorePlayer
def test_addScorePlayer():
    sb = ScoreBoard("Test", 3)
    sb.addScorePlayer(1)
    assert sb.getScorePlayer() == 1


# test addScoreAi
def test_addScoreAi():
    sb = ScoreBoard("Test", 3)
    sb.addScoreAi(1)
    assert sb.getScoreAi() == 1


# test game.py's game loop
def test_game_loop(capfd):
    game.game_loop()
    captured = capfd.readouterr()
    assert "You win the game!" in captured.out or "AI wins the game!" in captured.out
