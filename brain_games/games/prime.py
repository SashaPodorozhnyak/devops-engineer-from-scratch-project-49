import random
from brain_games.games.start_end import END_RANDOM, START_RANDOM


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(START_RANDOM, END_RANDOM)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer