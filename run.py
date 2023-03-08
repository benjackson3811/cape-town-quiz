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

def correct_answer():
    for question, options in questions.items():
        right_answer = options[0]
        sorted_options = sorted(options)
        for choice, option in enumerate(sorted_options):
            print(f" {choice}) {option}")

        answer_choice = int(input(f"{question}? "))
        answer = sorted_options[answer_choice]
        if answer == right_answer:
            print("That's right!")
        else:
            print(f"Incorrect! The answer is {right_answer!r}, not {answer!r}")


correct_answer()