from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUi

question_bank = []
for _ in question_data:
    question_bank.append(Question(_["question"], _["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_ui = QuizUi(quiz)

print("You have completed the quiz.")
print(f"You final score was: {quiz.score}/{len(question_bank)}")
