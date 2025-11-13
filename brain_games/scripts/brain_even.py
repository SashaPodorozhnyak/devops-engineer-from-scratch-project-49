from brain_games.games.cli import welcome_user
from brain_games.games.even import is_even
import random


def main():

    print('Welcome to the Brain Games!')
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1,100)
        print(f'Question: {number}')
        answer = input('Your answer: ').lower()
        correct_answer = 'yes' if is_even(number) else 'no'
        if correct_answer == answer:
            print('Correct!')
            i += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            return
    return print (f'Congratulations, {name}!')

if __name__ == "__main__":
    main()