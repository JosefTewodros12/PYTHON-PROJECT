class QuizBrain:
    # score = 0

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def still_have_questions(self):
        # try:
        return self.question_number < len(self.questions_list)
        # finally:
        #     print("You've completed the quiz.")
        #     print(f"Your final score is: {self.score}")

    def next_question(self):
        currentquestion = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {currentquestion.question} (True or False)?: ").lower()
        self.check_answer(user_answer, currentquestion.correct_answer)

    def check_answer(self, user_answer, correct_answer):
        # global score
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong!")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score {self.score}/{self.question_number}\n")
