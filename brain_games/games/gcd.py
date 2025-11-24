import random

START_RANDOM = 1
END_RANDOM = 100


def generate_question():
    number1 = random.randint(START_RANDOM, END_RANDOM)
    number2 = random.randint(START_RANDOM, END_RANDOM)
    question = f"{number1} {number2}"
    if number1 == 0:
        correct_answer = number2
    if number2 == 0:
        correct_answer = number1
    else:
        while number1 != 0 and number2 != 0:
            number1, number2 = number2, number1 % number2
        correct_answer = number1

    return question, str(correct_answer)
