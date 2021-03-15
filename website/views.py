from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/archer')
def archer():
    return render_template('/characters/archer.html')

@views.route('/knight')
def knight():
    return render_template('/characters/knight.html')

@views.route('/butcher')
def butcher():
    return render_template('/characters/butcher.html')

@views.route('/ghost')
def ghost():
    return render_template('/characters/ghost.html')

@views.route('/chef')
def chef():
    return render_template('/characters/chef.html')

@views.route('/ninja')
def ninja():
    return render_template('/characters/ninja.html')

