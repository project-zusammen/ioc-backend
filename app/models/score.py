from app import db
from datetime import datetime


class Score(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    score = db.Column(db.FLOAT, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"), nullable=False)
    exam_id = db.Column(db.BigInteger, db.ForeignKey("exam.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return "<Score {}>".format(self.score)
