from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from .serializer import UserSchema
from .models.tables import User


bp_login = Blueprint('login', __name__)


@bp_login.route('/login', methods=['POST'])
def login():
    result = {}
    user, error = UserSchema().load(request.json)

    if error:
        result = {'error': {'reason': error}}
        return jsonify(result), 401

    user = User.query.filter_by(username=user.username).first()

    if user and user.verify_token(request.json['password']):
        access_token = create_access_token(
            identity=user.user_id,
            expires_delta=timedelta(seconds=60)
        )
        refresh_token = create_refresh_token(identity=user.user_id)
        result = {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'message': 'success'
        }
        return jsonify(result), 200

    result = {'error': {'reason': 'credenciais inválidas'}}
    return jsonify(result), 401
