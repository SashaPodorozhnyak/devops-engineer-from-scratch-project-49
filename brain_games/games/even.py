import random

from brain_games.games.start_end import END_RANDOM, START_RANDOM


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = random.randint(START_RANDOM, END_RANDOM)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer
