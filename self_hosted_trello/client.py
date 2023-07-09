```python
from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('board_created')
def handle_board_created(data):
    print('Board Created: ' + str(data))

@socketio.on('list_created')
def handle_list_created(data):
    print('List Created: ' + str(data))

@socketio.on('card_created')
def handle_card_created(data):
    print('Card Created: ' + str(data))

@socketio.on('user_logged_in')
def handle_user_logged_in(data):
    print('User Logged In: ' + str(data))

if __name__ == '__main__':
    socketio.run(app)
```