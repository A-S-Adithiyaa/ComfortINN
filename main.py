from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df=pf.read_csv('login.csv')

print('hi hi')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        email=request.form.get('email')
        passw=request.form.get('passw')
        cpassw=request.form.get('cpassw')

    return render_template('signup.html')


@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email=request.form.get('email')
        passw=request.form.get('passw')
        print(email, passw)
        
    return render_template('signin.html')


if __name__ == '__main__':
    app.run(debug=True)
