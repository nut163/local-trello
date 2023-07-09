```python
from flask_sqlalchemy import SQLAlchemy
from self_hosted_trello.database import db

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    cards = db.relationship('Card', backref='list', lazy=True)

    def __init__(self, title, board_id):
        self.title = title
        self.board_id = board_id

    def create_list(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_lists_by_board_id(cls, board_id):
        return cls.query.filter_by(board_id=board_id).all()
```