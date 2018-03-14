from flask import (
  Flask,
  render_template,
  request,
  redirect,
)
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import BlogPost

@app.route('/')
def index():
  # get posts from database
  posts = BlogPost.query.all();
  return render_template('index.html', posts=posts)

@app.route('/blogpost', methods=['POST'])
@app.route('/blogpost/<id>', methods=['GET'])
def blogpost(id=None):
  if request.method == 'GET' and id is not None:
    # get post with id from database
    post = BlogPost.query.get(id)
    return render_template('blogpost.html', post=post)
  elif request.method == 'POST':
    # write form data (request.form) to database
    post = BlogPost(title=request.form['title'], body=request.form['body'])
    db.session.add(post)
    db.session.commit()
    return redirect('/')

@app.route('/newpost')
def newpost():
  return render_template('newpost.html')