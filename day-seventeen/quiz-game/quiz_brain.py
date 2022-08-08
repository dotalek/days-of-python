"""Defines the QuizBrain model.

It keeps track of the questions and correct answers from a player.
"""


class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def get_current_question(self):
        return self.question_list[self.question_number]

    def next_question(self):
        question = self.get_current_question()
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {question.text} (True/False) ")
        self.check_answer(answer, question.answer)
        self.print_score()
        print("\n")
        return

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's correct!")
            self.score += 1
        else:
            print("Sorry, that's wrong...")
        print(f"The right answer was: {correct_answer}")
        return

    def print_score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")
        return

    def print_final_score(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")
        return
