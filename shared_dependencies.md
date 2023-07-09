1. Exported Variables: 
   - `app` (main.py, server.py, client.py): Flask application instance.
   - `db` (main.py, database.py, user.py, board.py, list.py, card.py): SQLAlchemy database instance.

2. Data Schemas:
   - `User` (user.py, main.py, board.py, list.py, card.py): User data model.
   - `Board` (board.py, main.py, list.py, card.py): Board data model.
   - `List` (list.py, main.py, board.py, card.py): List data model.
   - `Card` (card.py, main.py, board.py, list.py): Card data model.

3. DOM Element IDs:
   - `board-container` (index.html, board.html, scripts.js): Container for all boards.
   - `list-container` (board.html, list.html, scripts.js): Container for all lists in a board.
   - `card-container` (list.html, card.html, scripts.js): Container for all cards in a list.
   - `user-profile` (index.html, user.html, scripts.js): User profile section.

4. Message Names:
   - `board_created` (server.py, client.py, scripts.js): Message for a new board creation.
   - `list_created` (server.py, client.py, scripts.js): Message for a new list creation.
   - `card_created` (server.py, client.py, scripts.js): Message for a new card creation.
   - `user_logged_in` (server.py, client.py, scripts.js): Message for user login.

5. Function Names:
   - `create_board` (main.py, board.py): Function to create a new board.
   - `create_list` (main.py, list.py): Function to create a new list.
   - `create_card` (main.py, card.py): Function to create a new card.
   - `login_user` (main.py, user.py): Function to login a user.
   - `init_db` (main.py, database.py): Function to initialize the database.
   - `run_server` (main.py, server.py): Function to run the server.
   - `connect_client` (main.py, client.py): Function to connect a client.

6. Shared Dependencies in requirements.txt:
   - Flask: A web framework used in main.py, server.py, and client.py.
   - SQLAlchemy: A SQL toolkit and ORM used in main.py, database.py, user.py, board.py, list.py, and card.py.
   - Jinja2: A templating language for Python, used in all HTML templates.
   - SocketIO: A library for real-time web applications, used in server.py and client.py.

7. Installation Instructions: 
   - Shared in README.md and installation.bat.