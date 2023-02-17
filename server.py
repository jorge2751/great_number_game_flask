from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret_key'

MAX_GUESSES = 5

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        if guess < session['number']:
            message = 'Your guess is too low!'
        elif guess > session['number']:
            message = 'Your guess is too high!'
        else:
            message = f'Congratulations, you guessed the number in {session["attempts"]} attempts!'
            session.pop('number')
            session.pop('attempts')
        if session.get('attempts', 0) >= MAX_GUESSES:
            message = 'You Lose'
            session.pop('number')
            session.pop('attempts')
        return render_template('index.html', message=message)
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)


