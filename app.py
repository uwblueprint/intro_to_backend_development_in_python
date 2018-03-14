from flask import (
  Flask,
  render_template,
  request,
  redirect,
  flash,
)
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

from models import BlogPost

app = Flask(__name__)

@app.route('/')
def index():
  # get posts from database
  posts = BlogPost.query.all();
  print(posts)
  return render_template('index.html', posts=posts)

@app.route('/blogpost', methods=['POST'])
@app.route('/blogpost/<id>', methods=['GET'])
def blogpost(id=None):
  if request.method == 'GET' and id is not None:
    # get post with id from database
    posts = BlogPost.query.get(id)
    print(posts)
    return render_template('blogpost.html', post=posts)
  elif request.method == 'POST':
    # write form data (request.form) to database
    post = BlogPost(title=request.form['title'], body=request.form['body'])
    db.session.add(post)
    db.session.commit()
    return redirect('/')

@app.route('/newpost')
def newpost():
  return render_template('newpost.html')

