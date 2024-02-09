from app import db
from datetime import datetime

class Exam(db.Model): 
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    question = db.Column(db.String(250), nullable=False)
    correct_option = db.Column(db.String(250), nullable=False)
    option_a = db.Column(db.String(250), nullable=False)
    option_b = db.Column(db.String(250), nullable=False)
    option_c = db.Column(db.String(250), nullable=False)
    option_d =  db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False) 
    material_id = db.Column(db.BigInteger, db.ForeignKey('material.id'), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    answers = db.relationship('Answer', backref='exam', lazy=True)
    scores = db.relationship('Score', backref='exam', lazy=True)
    def __repr__(self):
        return "<Exam {}>".format(self.name)