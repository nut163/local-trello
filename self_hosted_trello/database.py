```python
from flask_sqlalchemy import SQLAlchemy
from main import app

# Initialize SQLAlchemy with Flask application instance
db = SQLAlchemy(app)

def init_db():
    # Create all tables
    db.create_all()

    # Commit the changes
    db.session.commit()

if __name__ == "__main__":
    # Initialize the database
    init_db()
```