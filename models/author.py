from sqlalchemy.orm import relationship
from . import db

class Author(db.Model):
    __tablename__='authors'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String, nullable=False)

    books=relationship ('Book',back_populates='author',cascade='all, delete-orphan')

    def to_dict(self):
        {
            'id': self.id,
            'name': self.name,
        }
