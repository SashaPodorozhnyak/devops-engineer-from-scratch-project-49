from brain_games.games.cli import welcome_user
from brain_games.games.even import even
from brain_games.games.check_answer import check_answer


def main():

    print('Welcome to the Brain Games!')
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        answer, correct_answer = even()
        if not check_answer(answer, correct_answer, name):
            return
        i +=1
    return print (f'Congratulations, {name}!')

if __name__ == "__main__":
    main()