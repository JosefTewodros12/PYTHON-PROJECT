from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    question_bank.append(
        Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)
# quiz_continue = quiz.still_have_questions()
# while quiz_continue == True:
while quiz.still_have_questions():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score} / {len(question_bank)}")
