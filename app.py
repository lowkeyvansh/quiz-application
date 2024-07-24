from flask import Flask, render_template, request

app = Flask(__name__)

questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
}

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question, correct_answer in questions.items():
        if request.form.get(question) == correct_answer:
            score += 1
    return f'Your score: {score}/{len(questions)}'

if __name__ == '__main__':
    app.run(debug=True)
