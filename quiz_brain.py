

class QuizBrain:

    def __init__(self, q_list):
        self.quest_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self, q_list):
        return self.quest_number != len(q_list)

    def next_question(self):
        current_question = self.question_list[self.quest_number]
        self.quest_number += 1
        user_answer = input(f"Q.{self.quest_number}: {current_question.text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score} / {self.quest_number} \n")