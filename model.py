from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):  # Todo model define garne
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    done = db.Column(db.Boolean, default=False) # Default False so that done pathayana vana False rakhcha

    def __repr__(self):  # Object string representation define garne
        return f'<Todo {self.title}>'

# Automatically create the tables during application startup
with app.app_context():
    db.create_all()
