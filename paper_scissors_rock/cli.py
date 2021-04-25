from game import *

POSSES = {m.value: m for m in Move}


def human_decide() -> Move:
    while True:
        val = input(f"select input from {POSSES}: ")
        try:
            return POSSES[int(val)]
        except KeyError as e:
            print("invalid input")


def display(*vals):
    print(vals)


player = Player(human_decide)


def main():
    print(round(player, BASIC_AI, display))


if __name__ == "__main__":
    main()
