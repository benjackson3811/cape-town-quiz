# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Importing the libraries for the running of the quiz
"""
import random
from string import ascii_lowercase
from questions import NUM_QUESTIONS_PER_QUIZ
from questions import QUESTIONS


def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {num:}")
        num_correct += ask_question(question, options)


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def ask_question(question, options):
    right_answer = options[0]
    sorted_options = random.sample(options, k=len(options))

    answer = get_answer(question, sorted_options)
    if answer == right_answer:
        print("👍 That's right! ⭐")
        return 1
    else:
        print(f"Incorrect! The answer is {right_answer!r}, not {answer!r}")
        return 0


def get_answer(question, options):
    print(f"{question}?")
    sorted_options = dict(zip(ascii_lowercase, options))
    for choice, option in sorted_options.items():
        print(f" {choice}) {option}")

    while (answer_choice := input("\nChoice? ")) not in sorted_options:
        print(f"Please answer one of {', '.join(sorted_options)}")

    return sorted_options[answer_choice]


if __name__ == "__main__":
    run_quiz()
