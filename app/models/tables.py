"""Definition of database table models."""
from flask_sqlalchemy import SQLAlchemy
from passlib.handlers.sha2_crypt import sha512_crypt as hashcode


db = SQLAlchemy()

def configure_database(app):
    with app.app_context():
        db.init_app(app)
        app.db = db
        db.create_all()


class User(db.Model):
    """
    Users model.
    """
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def generate_hash(self):
        self.password = hashcode.hash(self.password)

    def verify_token(self, token):
        return hashcode.verify(token, self.password)

    def __repr__(self):
        return f'<User {self.username}>'
