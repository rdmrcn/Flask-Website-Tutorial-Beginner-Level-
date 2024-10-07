from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    done = db.Column(db.Boolean, default=False)
