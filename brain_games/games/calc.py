import random


def calc(number1, number2, operator):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2

def game_calc(operators):
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    operator = random.choice(operators)
    operators.remove(operator)
    print(f'Question: {number1} {operator} {number2}')
    answer = int(input('Your answer: '))
    correct_answer = calc(number1, number2, operator)
    return answer, correct_answer, operators