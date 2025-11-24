from brain_games.games.cli import welcome_user


def play_game(DESCRIPT, module_with_game):
    name = welcome_user()
    print(DESCRIPT)
    RAUNDS = 3
    for _ in range(RAUNDS):
        question, correct_answer = module_with_game.generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
