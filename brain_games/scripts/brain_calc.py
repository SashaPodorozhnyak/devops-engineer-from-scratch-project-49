from brain_games.games.cli import welcome_user
from brain_games.games.calc import calc, game_calc
from brain_games.games.check_answer import check_answer


def main():

    print('Welcome to the Brain Games!')
    name = welcome_user()

    print('What is the result of the expression?')
    i = 0
    operators =['+', '-', '*']
    while i < 3:
        answer, correct_answer, operators = game_calc(operators)
        if not check_answer(answer, correct_answer, name):
            return
        i += 1
    return print (f'Congratulations, {name}!')

if __name__ == "__main__":
    main()