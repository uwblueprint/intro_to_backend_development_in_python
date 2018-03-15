from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(64))
  body = db.Column(db.Text)
  date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  comments = db.relationship('BlogComment', backref='blog_post', lazy=True)

  def __repr__(self):
    return '<BlogPost {}>'.format(self.body)

class BlogComment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.Text)
  date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  blogpost_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'), nullable=False)

  def __repr__(self):
    return '<BlogComment {}>'.format(self.comment)
