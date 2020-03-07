from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '84b9f551270fa080b4fddd439acfd3fc'

users = [
    {
        'code': 'c110611',
        'fname': 'Mauro',
        'lname': 'Arima',
        'dt_nasc': 'July 24, 1967'
    },
    {

        'code': 'c999999',
        'fname': 'Helen',
        'lname': 'Marques',
        'dt_nasc': 'April 10, 1980'
    },
    {
        'code': 'c111111',
        'fname': 'Isabel',
        'lname': 'Cristina',
        'dt_nasc': 'January 01, 1977'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', users=users)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if(__name__ == '__main__'):
    app.run(debug=True)
