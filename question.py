
class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_choice):
        return user_choice == self.correct_option
