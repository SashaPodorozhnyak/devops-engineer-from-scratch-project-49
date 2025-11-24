from brain_games.games import even
from brain_games.games.engine import play_game


def main():
    DESCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(DESCRIPT, even)


if __name__ == "__main__":
    main()
