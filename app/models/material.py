from app import db
from datetime import datetime

class Material(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    category = db.relationship('Category', back_populates='materials', lazy=True)
    user_materials = db.relationship('User', back_populates='user_materials', lazy=True)
    exams = db.relationship('Exam', backref='material', lazy=True)
    comments = db.relationship("Comment", backref="material", lazy=True)
    scores = db.relationship('Score', backref='exam', lazy=True)

    def __repr__(self):
        return "<Material {}>".format(self.name)