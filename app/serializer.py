from app.models.tables import User
from marshmallow import fields
from flask_marshmallow import Marshmallow


marshmallow = Marshmallow()

def configure_marshmallow(app):
    marshmallow.init_app(app)


class UserSchema(marshmallow.ModelSchema):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = fields.Str(required=True)
    password = fields.Str(required=True)
