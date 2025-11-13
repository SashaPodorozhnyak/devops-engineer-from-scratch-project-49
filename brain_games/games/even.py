import random


def is_even(number):
    return number % 2 == 0

def even():
    number = random.randint(1,100)
    print(f'Question: {number}')
    answer = input('Your answer: ').lower()
    correct_answer = 'yes' if is_even(number) else 'no'
    return answer, correct_answer