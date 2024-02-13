from app import db
from datetime import datetime

class CommentReply(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    reply = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"), nullable=False)
    comment_id = db.Column(db.BigInteger, db.ForeignKey("comment.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="user_replies", lazy=True)
    comment = db.relationship("Comment", back_populates="replies", lazy=True)    
    def __repr__(self):
        return "<CommentReply {}".format(self.name)