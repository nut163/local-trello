```python
from flask import Flask, request
from flask_socketio import SocketIO, emit
from main import app, db, create_board, create_list, create_card, login_user

socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('board_created')
def handle_board_created(data):
    board = create_board(data['name'], data['user_id'])
    db.session.add(board)
    db.session.commit()
    emit('board_created', {'id': board.id, 'name': board.name}, broadcast=True)

@socketio.on('list_created')
def handle_list_created(data):
    list_ = create_list(data['name'], data['board_id'])
    db.session.add(list_)
    db.session.commit()
    emit('list_created', {'id': list_.id, 'name': list_.name, 'board_id': list_.board_id}, broadcast=True)

@socketio.on('card_created')
def handle_card_created(data):
    card = create_card(data['name'], data['list_id'])
    db.session.add(card)
    db.session.commit()
    emit('card_created', {'id': card.id, 'name': card.name, 'list_id': card.list_id}, broadcast=True)

@socketio.on('user_logged_in')
def handle_user_logged_in(data):
    user = login_user(data['username'], data['password'])
    if user:
        emit('user_logged_in', {'id': user.id, 'username': user.username}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
```