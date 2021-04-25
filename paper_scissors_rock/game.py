from enum import Enum
from typing import Optional, Callable
import random


class Move(Enum):
    PAPER = 0
    SCISSORS = 1
    ROCK = 2


class Player:
    def __init__(self, turn: Turn):
        self.turn = turn


Turn = Callable[[], Move]
Possibility = Optional[bool]
##Display:Callable[[Move, Move], None]


def _round(p1: Move, p2: Move) -> Possibility:
    if p1 == p2:
        return None
    return (p1.value - p2.value) % 3 == 1


def rev(p: Possibility) -> Possibility:
    if p is None:
        return None
    else:
        return not (p)


def rand():
    return random.choice(list(Move))


BASIC_AI = Player(rand)


def round(
    p1: Player, p2: Player, move_display: Callable[[Move, Move], None]
) -> Possibility:
    moves = [p1.turn(), p2.turn()]
    move_display(*moves)
    return _round(*moves)
