from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(64))
  body = db.Column(db.Text)
  date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __repr__(self):
    return '<BlogPost {}>'.format(self.body)