from app import db

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    replyTo = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Comments {}>'.format(self.comment)