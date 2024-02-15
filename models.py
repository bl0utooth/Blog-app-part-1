"""Models for Blogly."""

from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Windows_10_Default_Profile_Picture.svg/640px-Windows_10_Default_Profile_Picture.svg.png'

class User(db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, 
    primary_key=True)
    first_name = db.Column(db.Text, 
    nullable=False)
    last_name = db.Column(db.Text, 
    nullable=False)
    image_url = db.Column(db.Text, 
    nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    db.app = app
    db.init_app(app)