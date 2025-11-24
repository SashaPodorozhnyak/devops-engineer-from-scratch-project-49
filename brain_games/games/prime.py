import random

START_RANDOM = 1
END_RANDOM = 100


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(START_RANDOM, END_RANDOM)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer
