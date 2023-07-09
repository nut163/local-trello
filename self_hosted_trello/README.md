# Self-Hosted Trello

This is a self-hosted version of Trello that can be run on a Windows computer. It is a project management application that allows users to create boards, lists, and cards to organize and prioritize their projects in a fun, flexible, and rewarding way.

## Features

- User Authentication: Users can create an account and log in.
- Boards: Users can create, view, update, and delete boards.
- Lists: Within each board, users can create, view, update, and delete lists.
- Cards: Within each list, users can create, view, update, and delete cards.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory `self_hosted_trello`.
3. Run the `installation.bat` file to install the necessary dependencies.
4. Run `main.py` to start the application.

## Dependencies

- Flask: A web framework used for creating the application.
- SQLAlchemy: A SQL toolkit and ORM used for database operations.
- Jinja2: A templating language for Python, used for rendering the views.
- SocketIO: A library for real-time web applications, used for real-time updates.

## File Structure

- `main.py`: The main application file.
- `board.py`: Contains the Board data model and related operations.
- `card.py`: Contains the Card data model and related operations.
- `list.py`: Contains the List data model and related operations.
- `user.py`: Contains the User data model and related operations.
- `database.py`: Contains the database configuration and initialization.
- `server.py`: Contains the server-side operations.
- `client.py`: Contains the client-side operations.
- `static/css/styles.css`: Contains the CSS styles for the application.
- `static/js/scripts.js`: Contains the JavaScript for the application.
- `templates/`: Contains the HTML templates for the application views.

## Usage

After running `main.py`, open your web browser and navigate to `localhost:5000` to start using the application.