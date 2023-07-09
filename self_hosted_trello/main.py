```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server import run_server
from client import connect_client
from user import login_user
from board import create_board
from list import create_list
from card import create_card
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return login_user()

@app.route('/board', methods=['POST'])
def board():
    return create_board()

@app.route('/list', methods=['POST'])
def list():
    return create_list()

@app.route('/card', methods=['POST'])
def card():
    return create_card()

if __name__ == "__main__":
    init_db()
    run_server()
    connect_client()
```