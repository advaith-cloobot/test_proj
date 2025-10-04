"""
Authentication utilities
"""
import hashlib
from db_ops.user_operations import get_user_by_email

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    """Verify a password against its hash"""
    return hash_password(password) == hashed_password

def authenticate_user(email, password):
    """
    Authenticate a user with email and password
    Returns user data if authentication is successful, None otherwise
    """
    try:
        user = get_user_by_email(email)
        
        if user and verify_password(password, user['password']):
            # Remove password from returned user data
            user_data = user.copy()
            del user_data['password']
            return user_data
        
        return None
        
    except Exception as e:
        print(f"Authentication error: {e}")
        return None

def generate_token(user_id):
    """
    Generate a simple token for user authentication
    In production, use JWT or similar secure token generation
    """
    import time
    import hashlib
    
    timestamp = str(int(time.time()))
    token_data = f"{user_id}:{timestamp}"
    token = hashlib.sha256(token_data.encode()).hexdigest()
    
    return token

def validate_token(token):
    """
    Validate a user token
    In production, implement proper JWT validation
    """
    # Simplified token validation for demo
    return token is not None and len(token) > 10
