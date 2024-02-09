from app import db
from datetime import datetime

class Answer(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    answer = db.Column(db.String(250), nullable=False)
    exam_id = db.Column(db.BigInteger, db.ForeignKey('exam.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return "<Answer {}>".format(self.name)