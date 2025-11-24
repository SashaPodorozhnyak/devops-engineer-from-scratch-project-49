from brain_games.games import progression
from brain_games.games.engine import play_game


def main():
    DESCRIPT = "What number is missing in the progression?"
    play_game(DESCRIPT, progression)


if __name__ == "__main__":
    main()
