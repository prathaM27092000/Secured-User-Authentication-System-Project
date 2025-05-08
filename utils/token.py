# token.py
import jwt
from flask import request, jsonify
from functools import wraps
from config import Config
from models.user import get_user_by_username

def generate_token(user):
    payload = {
        'username': user['username'],
        'role': user['role']
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    if isinstance(token, bytes):  # Handle byte-string for compatibility
        token = token.decode('utf-8')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Authorization header is missing'}), 403

        if not auth_header.startswith('Bearer '):
            return jsonify({'message': 'Authorization header must start with Bearer'}), 403

        token = auth_header.split(" ")[1]

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            user = get_user_by_username(data['username'])
            if not user:
                raise Exception('User not found')
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 403
        except jwt.InvalidTokenError as e:
            return jsonify({'message': f'Token is invalid: {str(e)}'}), 403
        except Exception as e:
            return jsonify({'message': f'Authentication error: {str(e)}'}), 403

        return f(user, *args, **kwargs)
    return decorated
