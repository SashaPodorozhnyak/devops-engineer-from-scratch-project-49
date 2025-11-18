import random


def generate_question():
   
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    if number1 == 0: 
        correct_answer = number2
    if number2 == 0: 
        correct_answer = number1
    else:
        while number1 != 0 and number2 != 0:
            number1, number2 = number2, number1 % number2
        correct_answer = number1

    return question, str(correct_answer)

