class QuizBrain:

    def __init__(self, question_list):
        """Init variables"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Check if more question is left"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Go to next question"""
        question = self.question_list[self.question_number].text
        answer = input(f"Q.{self.question_number+1}: {question} (True/False)?: ")
        correct_answer = self.question_list[self.question_number].answer
        self.check_answer(answer, correct_answer)
        print(f"your current score is: {self.score}/{self.question_number+1}")
        print('\n')
        self.question_number += 1

    def check_answer(self, answer, correct_answer):
        """Check if the answer is correct"""
        if answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong")
        print(f"Correct answer: {correct_answer}.")

