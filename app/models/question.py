from app import db
from datetime import datetime

class Question(db.Model): 
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    question_text = db.Column(db.String(250), nullable=False)
    question_number = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(250), nullable=False)
    option_a = db.Column(db.String(250), nullable=False)
    option_b = db.Column(db.String(250), nullable=False)
    option_c = db.Column(db.String(250), nullable=False)
    option_d =  db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False) 
    exam_id = db.Column(db.BigInteger, db.ForeignKey('exam.id'), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    answers = db.relationship('Answer', backref='question', lazy=True)
    
    def __repr__(self):
        return "<Question {}>".format(self.name)