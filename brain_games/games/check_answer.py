


def check_answer(answer, correct_answer, name):
    if correct_answer == answer:
        print('Correct!')
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
        print(f"Let's try again, {name}!")
        return False
    return True