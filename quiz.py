
from question import Question
import json

class Quiz:
    def __init__(self, category, file_path):
        self.category = category
        self.file_path = file_path
        self.questions = []
        self.score = 0

    def load_questions(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        for q in data:
            self.questions.append(
                Question(q["question"], q["options"], q["answer"])
            )

    def start_quiz(self):
        print(f"\nStarting Quiz: {self.category}")
        for idx, q in enumerate(self.questions, start=1):
            print(f"\nQ{idx}. {q.question_text}")
            for i, opt in enumerate(q.options, start=1):
                print(f"{i}. {opt}")
            choice = int(input("Your choice: ")) - 1
            if q.is_correct(choice):
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")

    def show_result(self):
        total = len(self.questions)
        percent = (self.score / total) * 100
        print(f"\nScore: {self.score}/{total} ({percent:.2f}%)")
        if percent >= 80:
            print("Feedback: Excellent")
        elif percent >= 50:
            print("Feedback: Good Try")
        else:
            print("Feedback: Try Again")
