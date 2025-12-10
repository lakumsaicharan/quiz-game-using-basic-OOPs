class QuizBrain:
    def __init__(self,quiz_list):
        self.question_number = 0
        self.score = 0
        self.quiz_list = quiz_list
    def next_question(self):
        current_question = self.quiz_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q {self.question_number} {current_question.text} True/False: ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number<len(self.quiz_list):
            return True
        else:
            return False
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You are right!\nyou got {self.score}/{self.question_number}\nplease proceed to the next question.')
        else:
            print(f'You are wrong!\nyou got {self.score}/{self.question_number}\nplease proceed to the next question.')
        print(f'The correct answer was: {correct_answer}.')