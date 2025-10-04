from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

# Import modules
from utils.auth import authenticate_user
from db_ops.user_operations import get_user_by_email, create_user
from constants.api_responses import API_RESPONSES

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Flask server is running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/auth/login', methods=['POST'])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'email' not in data or 'password' not in data:
            return jsonify(API_RESPONSES['INVALID_REQUEST']), 400
        
        email = data['email']
        password = data['password']
        
        # Authenticate user
        user = authenticate_user(email, password)
        
        if user:
            return jsonify({
                'status': 'success',
                'message': 'Login successful',
                'user': {
                    'id': user['id'],
                    'email': user['email'],
                    'name': user.get('name', 'User')
                }
            }), 200
        else:
            return jsonify(API_RESPONSES['INVALID_CREDENTIALS']), 401
            
    except Exception as e:
        return jsonify(API_RESPONSES['SERVER_ERROR']), 500

@app.route('/api/auth/register', methods=['POST'])
def register():
    """User registration endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'email' not in data or 'password' not in data:
            return jsonify(API_RESPONSES['INVALID_REQUEST']), 400
        
        email = data['email']
        password = data['password']
        name = data.get('name', '')
        
        # Check if user already exists
        existing_user = get_user_by_email(email)
        if existing_user:
            return jsonify(API_RESPONSES['USER_EXISTS']), 409
        
        # Create new user
        user = create_user(email, password, name)
        
        if user:
            return jsonify({
                'status': 'success',
                'message': 'User created successfully',
                'user': {
                    'id': user['id'],
                    'email': user['email'],
                    'name': user.get('name', '')
                }
            }), 201
        else:
            return jsonify(API_RESPONSES['CREATION_FAILED']), 500
            
    except Exception as e:
        return jsonify(API_RESPONSES['SERVER_ERROR']), 500

@app.route('/api/user/profile', methods=['GET'])
def get_profile():
    """Get user profile endpoint"""
    try:
        # In a real app, you'd get user ID from JWT token
        user_id = request.headers.get('X-User-ID')
        
        if not user_id:
            return jsonify(API_RESPONSES['UNAUTHORIZED']), 401
        
        # Get user profile (simplified for demo)
        return jsonify({
            'status': 'success',
            'user': {
                'id': user_id,
                'email': 'user@example.com',
                'name': 'Demo User'
            }
        }), 200
        
    except Exception as e:
        return jsonify(API_RESPONSES['SERVER_ERROR']), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify(API_RESPONSES['NOT_FOUND']), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify(API_RESPONSES['SERVER_ERROR']), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
