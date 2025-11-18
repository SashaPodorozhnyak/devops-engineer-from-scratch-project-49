import random


def generate_progression(start, size, step):
    progression = []
    for index in range(0, size + 1):
        progression.append(str(start + index * step))
    return progression


def generate_question():
    start = random.randint(1, 50)
    size = random.randint(5, 10)
    step = random.randint(1, 20)
    index_answer = random.randint(0, size)
    question = generate_progression(start, size, step)
    correct_answer = question[index_answer]
    question[index_answer] = ".."
    question = " ".join(question)
    return question, correct_answer
