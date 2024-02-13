from app import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"), nullable=False)
    material_id = db.Column(db.BigInteger, db.ForeignKey("material.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="comments", lazy=True)
    replies = db.relationship("CommentReply", back_populates="comment", lazy=True)

    def __repr__(self):
        return "<Comment {}>".format(self.name)