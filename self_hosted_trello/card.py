```python
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base, db

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(200))
    list_id = Column(Integer, ForeignKey('lists.id'))

    def __init__(self, title, description, list_id):
        self.title = title
        self.description = description
        self.list_id = list_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_list_id(cls, list_id):
        return cls.query.filter_by(list_id=list_id).all()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
```