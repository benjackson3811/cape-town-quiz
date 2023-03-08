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


def prepare_questions(questions, num_questions):
    """
    function to define the question to be asked and their question number
    """
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, option):
    """
    function to identify the correct answer to the question asked to the user,
    """
    print(f"{question}?")
    sorted_options = dict(zip(ascii_lowercase, options))
    for choice, option in sorted_options.items():
        print(f" {choice}) {option}")

    return sorted_options[answer_choice]


def ask_question(question, options):
    """
    NEED DESCRIPTION
    """
    right_answer = options[0]
    sorted_options = random.sample(options, k=len(options))

    answer = get_answer(question, sorted_options)
    if answer == right_answer:
        print("👍 That's right! ⭐")
        return 1
    else:
        print(f"Incorrect! The answer is {right_answer!r}, not {answer!r}")
        return 0


def run_quiz():
    """
    NEED DESCRIPTION
    """
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (questions, options) in enumerate(questions, start=1):
        print(f"\nYou got {num_correct} correct out of {num} questions")

    if __name__ == "__main__":
        run_quiz()

run_quiz()
