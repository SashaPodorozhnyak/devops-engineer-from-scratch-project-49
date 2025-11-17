from brain_games.games import gcd
from brain_games.games.engine import play_game


def main():
    descrip = 'Find the greatest common divisor of given numbers.'
    play_game(descrip, gcd)

if __name__ == "__main__":
    main()