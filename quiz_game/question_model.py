class Question:

    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer


class QuizBrain:

    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def still_has_q(self):
        return self.q_number < len(self.q_list)


    def next_q(self):
        current_q = (self.q_list[self.q_number])
        self.q_number += 1
        awnser = input(f"Q.{self.q_number}: {current_q.text} (True/False)?: ")
        self.check_answer(awnser, current_q.answer)

    def check_answer(self, ans, correct_answer):
        if ans.lower() == correct_answer.lower():
            print("You got it !")
            self.score += 1
        else:
            print("Thats wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}")
        print()
