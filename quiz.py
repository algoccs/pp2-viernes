from flask import Flask, redirect, url_for, session, request
from database import get_next_question, get_quises

# TRABAJANDO CON SESSION
app = Flask(__name__)
app.config['SECRET_KEY'] = 'NoTieneClave'

def start_quiz(quiz_id):
    session['quiz'] = quiz_id
    session['prev_question'] = 0

def end_quiz():
    session.clear()


def form_html():
    quises = get_quises()

    options = ''
    for id, name in quises:
        options += f'<option value="{id}">{name}</option>\n'


    html_template = f'''
        <html lang="en">
        <body>
            <h2>Seleccione un cuestionario:</h2>
            <form action="/" method="post">
                <select name="quiz">
                    {options}
                </select>
                <p><input type="submit" value="Seleccionar"></p>
            </form>
        </body>
        </html>
    '''

    return html_template

def index():
    if request.method == 'GET':
        end_quiz()
        return form_html()

    else:
        quiz_id = request.form.get('quiz')
        start_quiz(quiz_id)
        return redirect(url_for('test'))

def test():
    result = get_next_question(session['prev_question'], session['quiz'])
    if result is None or result == 0:
        return redirect(url_for('result'))
    else:
        session['prev_question'] = result[0]

    return f'<h1>{result}</h1>'

    
def result():
    return 'RESULTADO DEL TEST'


app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)


app.run()
