import random

START_RANDOM = 1
END_RANDOM = 20
START_SIZE_RANDOM = 5


def generate_progression(start, size, step):
    progression = []
    for index in range(0, size + 1):
        progression.append(str(start + index * step))
    return progression


def generate_question():
    start = random.randint(START_RANDOM, END_RANDOM)
    size = random.randint(START_SIZE_RANDOM, END_RANDOM)
    step = random.randint(START_RANDOM, END_RANDOM)
    index_answer = random.randint(0, size)
    question = generate_progression(start, size, step)
    correct_answer = question[index_answer]
    question[index_answer] = ".."
    question = " ".join(question)
    return question, correct_answer
