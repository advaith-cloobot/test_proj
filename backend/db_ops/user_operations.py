"""
User database operations
"""
import uuid
from datetime import datetime
from utils.auth import hash_password

# In-memory storage for demo purposes
# In production, use a proper database like PostgreSQL, MySQL, or MongoDB
users_db = {}

def get_user_by_email(email):
    """
    Get user by email address
    Returns user data if found, None otherwise
    """
    try:
        # Search for user by email
        for user_id, user_data in users_db.items():
            if user_data['email'].lower() == email.lower():
                return user_data
        return None
    except Exception as e:
        print(f"Error getting user by email: {e}")
        return None

def get_user_by_id(user_id):
    """
    Get user by ID
    Returns user data if found, None otherwise
    """
    try:
        return users_db.get(user_id)
    except Exception as e:
        print(f"Error getting user by ID: {e}")
        return None

def create_user(email, password, name=''):
    """
    Create a new user
    Returns user data if successful, None otherwise
    """
    try:
        # Check if user already exists
        if get_user_by_email(email):
            return None
        
        # Generate unique user ID
        user_id = str(uuid.uuid4())
        
        # Create user data
        user_data = {
            'id': user_id,
            'email': email.lower(),
            'password': hash_password(password),
            'name': name,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        # Store user in database
        users_db[user_id] = user_data
        
        # Return user data without password
        user_response = user_data.copy()
        del user_response['password']
        
        return user_response
        
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def update_user(user_id, **kwargs):
    """
    Update user data
    Returns updated user data if successful, None otherwise
    """
    try:
        if user_id not in users_db:
            return None
        
        # Update allowed fields
        allowed_fields = ['name', 'email']
        for field, value in kwargs.items():
            if field in allowed_fields:
                users_db[user_id][field] = value
        
        # Update timestamp
        users_db[user_id]['updated_at'] = datetime.now().isoformat()
        
        # Return updated user data without password
        user_data = users_db[user_id].copy()
        del user_data['password']
        
        return user_data
        
    except Exception as e:
        print(f"Error updating user: {e}")
        return None

def delete_user(user_id):
    """
    Delete a user
    Returns True if successful, False otherwise
    """
    try:
        if user_id in users_db:
            del users_db[user_id]
            return True
        return False
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False

def get_all_users():
    """
    Get all users (for admin purposes)
    Returns list of user data without passwords
    """
    try:
        users = []
        for user_data in users_db.values():
            user_response = user_data.copy()
            del user_response['password']
            users.append(user_response)
        return users
    except Exception as e:
        print(f"Error getting all users: {e}")
        return []
