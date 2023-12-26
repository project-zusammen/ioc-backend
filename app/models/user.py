from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    grade = db.Column(db.String(250))
    school = db.Column(db.String(250))
    role = db.Column(db.String(250), nullable=False)
    dob = db.Column(db.DateTime(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)