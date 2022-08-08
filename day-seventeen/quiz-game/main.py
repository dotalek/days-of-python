"""CLI Quiz game program.

Answer as many True/False questions as you can.
"""

import sys
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def main():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["question"], question["correct_answer"]))
    brain = QuizBrain(question_bank)
    while brain.still_has_questions():
        brain.next_question()
    brain.print_final_score()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
