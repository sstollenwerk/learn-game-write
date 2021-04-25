from hypothesis import given
import hypothesis.strategies as st

import game

move = st.sampled_from(game.Move)


def test_basic():
    assert game._round(game.Move.PAPER, game.Move.SCISSORS) == False
    assert game._round(game.Move.SCISSORS, game.Move.SCISSORS) == None
    assert game._round(game.Move.PAPER, game.Move.ROCK) == True


@given(move, move)
def test_symmetric(p1, p2):
    assert game._round(p1, p2) == game.rev(game._round(p2, p1))
