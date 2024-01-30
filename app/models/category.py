from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    materials = db.relationship("Material", back_populates="category", lazy=True)    
    def __repr__(self):
        return "<Category {}>".format(self.name)
