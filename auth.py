from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import create_user, get_user_by_username
from utils.token import generate_token, token_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    
    # Check if user already exists
    if get_user_by_username(username):
        return jsonify({'message': 'Username already exists'}), 409  # 409 Conflict

    password = generate_password_hash(data['password'])
    role = data.get('role', 'user')
    create_user(username, password, role)
    return jsonify({'message': 'User registered successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = get_user_by_username(data['username'])
    if user and check_password_hash(user['password'], data['password']):
        token = generate_token(user)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({'message': f'Welcome {current_user["username"]}, this is a protected route!'})

