import html


class QuizBrain:
    """Init all the methods to read and check the question against the answer"""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Check if there is still more questions"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Return the next question"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # escape the html specials characters
        text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {text}"

    def check_answer(self, user_answer):
        """Check if the answer is correct or not"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False

