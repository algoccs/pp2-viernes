from flask import Flask, redirect, url_for, session, request, render_template
from database import get_next_question, get_quises

# TRABAJANDO CON SESSION
app = Flask(__name__)
app.config['SECRET_KEY'] = 'NoTieneClave'

def start_quiz(quiz_id):
    session['quiz'] = quiz_id
    session['prev_question'] = 0
    session['totals'] = 0
    session['corrects'] = 0

def end_quiz():
    session.clear()

def check_answer():
    user_answer = request.form.get('ans_text')
    correct_answer = session['prev_correct_ans']

    if user_answer:
        session['totals'] += 1
        if user_answer == correct_answer:
            session['corrects'] += 1


def index():
    if request.method == 'GET':
        end_quiz()
        quises_list = get_quises()
        return render_template('index.html', quises=quises_list)

    else:
        quiz_id = request.form.get('quiz')
        start_quiz(quiz_id)
        return redirect(url_for('test'))

def test():
    if 'quiz' not in session:
        return redirect.url_for('index')

    if request.method == 'POST':
        check_answer()

    result = get_next_question(session['prev_question'], session['quiz'])

    if result is None or result == 0:
        return redirect(url_for('result'))

    session['prev_question'] = result[0]
    session['prev_correct_ans'] = result[2] # RESPUESTA CORRECTA

    question = result[1]
    options = list(result[2:6])

    return render_template('test.html', pregunta=question, opciones=options)

    
def result():
    return 'RESULTADO DEL TEST'


app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['GET', 'POST'])
app.add_url_rule('/result', 'result', result)


app.run(debug=True)
