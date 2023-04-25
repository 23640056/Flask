from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
     user = {'username': 'Zarif'}
     posts = [
     {
	  'author': {'username': 'John'},
	  'body': 'Beautiful day in Perth!'
     },
     {
	  'author': {'username': 'Susan'},
	  'body': 'The Avengers movie was so cool!'
     }
     ]
     return render_template("index.html", title="Home", user=user,
posts=posts)

@app.route('/button')
def button():
	return render_template("button.html", title="Button!")
