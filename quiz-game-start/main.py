from data import question_data
from quiz_brain import QuizBrain

import random

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_book = []
for q_data in question_data:
    new_question = Question(q_data['text'], q_data['answer'])
    question_book.append(new_question)

new_quiz = QuizBrain(question_book)
while new_quiz.question_rem():
    user_answer = new_quiz.next_question()
    answer = new_quiz.answer_checker(user_answer)
    if not answer:
        break
