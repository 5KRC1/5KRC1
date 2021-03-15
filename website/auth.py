from flask import Blueprint, render_template, request, flash, redirect


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        return redirect('/')
    else:
        return render_template('login.html')

@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        username = request.form['userName']
        password = request.form['password']

        print(email, username, password)
        return redirect('/')
    else:
        return render_template('signup.html')