
from question_model import Question
# from random import choice
from data import question_data
from quiz_brain import QuizBrain

# choice to get the elements
# q_text = choice(question_data)["text"]
# q_ans = choice(question_data)["answer"]
# quest = Question(q_text,q_ans)

question_bank = []
for quest in question_data:
    new_quest = Question(quest["text"], quest["answer"])
    question_bank.append(new_quest)

quiz = QuizBrain(question_bank)
while quiz.still_has_question(question_bank):
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score is {quiz.score} / {quiz.quest_number}!!")
