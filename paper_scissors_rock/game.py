from enum import Enum
from typing import Optional

class Move(Enum):
    PAPER = 0
    SCISSORS = 1
    ROCK = 2

Possibility = Optional[bool]

def _round(p1:Move, p2:Move) -> Possibility:
    if p1 == p2: return None
    return (p1.value - p2.value) % 3 == 1

def rev(p:Possibility) -> Possibility:
    if p is None:
        return None
    else:
        return not(p)
