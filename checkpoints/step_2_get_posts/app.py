from flask import (
  Flask,
  render_template,
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
