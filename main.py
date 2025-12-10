from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    q1 = i['text']
    a1 = i['answer']
    question_bank.append(Question(q1,a1))
print(question_bank[0])

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')