from flask import Blueprint, request, jsonify, current_app
from .serializer import UserSchema


bp_user = Blueprint('user', __name__)

@bp_user.route('/register', methods=['POST'])
def register():
    """function of the new user registration route."""
    result = {}
    schema = UserSchema()

    user, error = schema.load(request.json)

    if not error:
        user.generate_hash()
        current_app.db.session.add(user)
        current_app.db.session.commit()
        return schema.jsonify(user), 201
    else:
        result = {"error": {"reason": error}}
        print(error)
        return jsonify(result), 401
