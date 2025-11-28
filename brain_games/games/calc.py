import random

from brain_games.games.start_end import END_RANDOM, START_RANDOM

OPERATORS = ("+", "-", "*")


def generate_question():
    number1 = random.randint(START_RANDOM, END_RANDOM)
    number2 = random.randint(START_RANDOM, END_RANDOM)
    operator = random.choice(OPERATORS)

    def remove_operator(operator):
        global OPERATORS  # работаем с переменной из внешней области
        OPERATORS = tuple(item for item in OPERATORS if item != operator)
        return OPERATORS

    question = str(number1) + " " + str(operator) + " " + str(number2)
    correct_answer = calc(number1, number2, operator)
    remove_operator(operator)
    return str(question), str(correct_answer)


def calc(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2