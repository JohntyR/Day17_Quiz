from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

my_quiz_brain = QuizBrain(question_bank)

while my_quiz_brain.still_has_questions():
    my_quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {my_quiz_brain.score}/{my_quiz_brain.question_number}")