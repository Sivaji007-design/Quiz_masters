import os
from quiz import Quiz

class QuizManager:
    def __init__(self, data_folder):
        self.data_folder = data_folder

    def start(self):
        categories = os.listdir(self.data_folder)
        print("Available Categories:")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat.replace('.json','')}")
        
        choice = int(input("Select category: ")) - 1
        file_name = categories[choice]
        category = file_name.replace(".json","")

        quiz = Quiz(category, os.path.join(self.data_folder, file_name))
        quiz.load_questions()
        quiz.start_quiz()
        quiz.show_result()

    def get_categories(self):
        categories = [cat.replace('.json', '') for cat in os.listdir(self.data_folder)]
        return categories

    def get_questions(self, category):
        file_name = f"{category}.json"
        quiz = Quiz(category, os.path.join(self.data_folder, file_name))
        quiz.load_questions()
        return quiz.questions

    def evaluate_quiz(self, category, user_answers):
        file_name = f"{category}.json"
        quiz = Quiz(category, os.path.join(self.data_folder, file_name))
        quiz.load_questions()
        score = 0
        for idx, question in enumerate(quiz.questions):
            if question.is_correct(int(user_answers.get(str(idx), -1))):
                score += 1
        total = len(quiz.questions)
        percent = (score / total) * 100
        feedback = ""
        if percent >= 80:
            feedback = "Excellent"
        elif percent >= 50:
            feedback = "Good Try"
        else:
            feedback = "Try Again"
        return score, total, feedback
