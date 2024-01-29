from app import db
from datetime import datetime


class Exam(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    material_id = db.Column(
        db.BigInteger,
    )
    question = db.Column(db.String(250), nullable=False)
    created_by = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
