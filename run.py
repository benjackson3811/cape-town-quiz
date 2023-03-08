# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Importing the libraries for the running of the quiz
"""
import sys
import os
import time
from time import sleep
from questions import questions
from string import ascii_lowercase

def correct_answer():
    """
    defining the question asked to user, providing options, the correct answer and the score.
    """
    num_correct = 0
    for num, (question, options) in enumerate(questions.items(),start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        right_answer = options[0]
        sorted_options = dict(zip(ascii_lowercase,sorted(options)))
        for choice, option in sorted_options.items():
            print(f" {choice}) {option}")

        answer_choice = input("\nChoice? ")
        answer = sorted_options.get(answer_choice)
        if answer == right_answer:
            print("👍 That's right! 👍")
            num_correct +=1
        else:
            print(f"👎 Incorrect! 👎 The answer is {right_answer!r}, not {answer!r}")



