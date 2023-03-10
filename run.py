# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Importing the libraries for the running of the quiz
"""
import random
import os
import time
from string import ascii_uppercase
from questions import sea_questions


def quiz_logo():
    """
    Quiz logo
    """
    print("       ***** 🇿🇦 🌎Cape Town Quiz ! 📣☀ *****                    ")
    print()
    print("         As a current resident of Cape Town.                    ")
    print()
    print("       I have built a simple multiple choice quiz               ")
    print()
    print("              To celebrate the city                             ")
    print()
    print("  here are questions on of three topic that define Cape Town.   ")
    time.sleep(2)
    clear_screen()


def instructions():
    """
    the rules of the game! Guide to the user on what they can and cant do.
    """
    print("Welcome to the Quiz!")
    print()
    print("                The Rules of the Quiz                        ")
    time.sleep(2)
    print("You will have a choice of three quiz topics to choose from:  ")
    # ----------------------------------------------------------------
    clear_screen()
    print("             For each topic you answer 5 questions            ")
    print("             You can only answer A, B, C or D                 ")
    #  ---------------------------------------------------------------
    print("             You will know your answer sraight away           ")
    print("                     If correct great!                        ")
    print("                    If not, thats ok!                         ")
    clear_screen()
    print("       Choose 1,2 or 3 to answer questions on that topic      ")
    #  ---------------------------------------------------------------
    print("              1) The Sea 💺                                   ")
    print("              2) 🐮 Cape Town History                         ")
    print("              3) 🐆 Land Animals of Africa  🐅                ")
    time.sleep(2)
    
    print("                At the end of the quiz.                       ")
    print("                You will see your total score.                ")
    print("                Then you can try and beat it!                 ")

    input("press a button to continue \n")
    clear_screen()


def run_quiz():
    NUM_QUESTIONS_PER_QUIZ = 5
    right_answer = []


    questions = prepare_questions(
        sea_questions, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, options) in enumerate(questions, start=1):
        print("------------------")
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
    sorted_options = dict(zip(ascii_uppercase, options))
    for choice, option in sorted_options.items():
        print(f" {choice}) {option}")

    while (answer_choice := input("\nChoice? ")) not in sorted_options:
        print(f"Please answer one of {', '.join(sorted_options)}")

    return sorted_options[answer_choice]


def clear_screen():
    """
    Function to clear the screen.
    """
    os.system('clear')



def start():
    """
    start function, shows the main image, instructions then runs the quiz.
    """
    quiz_logo()
    instructions()
    run_quiz()
    


if __name__ == "__main__":
    start()


