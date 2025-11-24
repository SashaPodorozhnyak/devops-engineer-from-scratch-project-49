from brain_games.games import calc
from brain_games.games.engine import play_game


def main():
    DESCRIPT = "What is the result of the expression?"
    play_game(DESCRIPT, calc)


if __name__ == "__main__":
    main()
