from sqlalchemy.orm import relationship
from . import db

class Genre(db.Model):
    __tablename__='genres'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String, nullable=False)

    books=relationship('Book',back_populates='genre',cascade='all, delete-orphan')

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
    }
