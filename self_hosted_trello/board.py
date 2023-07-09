```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, db

class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='boards')
    lists = relationship('List', back_populates='board')

    def __init__(self, title, user_id):
        self.title = title
        self.user_id = user_id

    def create_board(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_board_by_id(board_id):
        return db.session.query(Board).filter_by(id=board_id).first()

    @staticmethod
    def get_all_boards():
        return db.session.query(Board).all()

    def delete_board(self):
        db.session.delete(self)
        db.session.commit()
```