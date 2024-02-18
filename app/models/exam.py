from app import db
from datetime import datetime

class Exam(db.Model): 
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False) 
    material_id = db.Column(db.BigInteger, db.ForeignKey('material.id'), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    questions = db.relationship('Question', backref='exam', lazy=True)
    scores = db.relationship("Score", backref='exam', lazy=True)

    def __repr__(self):
        return "<Exam {}>".format(self.name)