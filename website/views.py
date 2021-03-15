from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/archer')
def archer():
    return render_template('archer.html')

@views.route('/knight')
def knight():
    return render_template('knight.html')

@views.route('/butcher')
def butcher():
    return render_template('butcher.html')

@views.route('/ghost')
def ghost():
    return render_template('ghost.html')

@views.route('/chef')
def chef():
    return render_template('chef.html')

@views.route('/ninja')
def ninja():
    return render_template('ninja.html')

