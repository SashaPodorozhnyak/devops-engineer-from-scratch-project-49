from brain_games.games import prime
from brain_games.games.engine import play_game


def main():
    descrip = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(descrip, prime)


if __name__ == "__main__":
    main()
