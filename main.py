from flask import Flask, render_template, request, redirect, url_for
from quiz_manager import QuizManager

app = Flask(__name__)
manager = QuizManager("data")

@app.route('/')
def home():
    categories = manager.get_categories()
    return render_template('home.html', categories=categories)

@app.route('/quiz/<category>', methods=['GET', 'POST'])
def quiz(category):
    if request.method == 'POST':
        user_answers = request.form
        score, total, feedback = manager.evaluate_quiz(category, user_answers)
        return render_template('result.html', score=score, total=total, feedback=feedback)

    questions = manager.get_questions(category)
    return render_template('quiz.html', category=category, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
