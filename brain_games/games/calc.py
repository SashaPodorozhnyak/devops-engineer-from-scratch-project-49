import random

operators =['+', '-', '*']
def generate_question():
   
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    operator = random.choice(operators)

    def remove_operator(operator):
        global operators # говорим, что работаем с переменной из внешней области
        operators.remove(operator)
        return operators
   
   
    question = str(number1) + ' ' + str(operator) + ' ' + str(number2)
    correct_answer = calc(number1, number2, operator)
    remove_operator(operator)
    return str(question), str(correct_answer)



def calc(number1, number2, operator):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
