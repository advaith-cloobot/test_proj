"""
API response constants for consistent error handling
"""

API_RESPONSES = {
    'SUCCESS': {
        'status': 'success',
        'message': 'Operation completed successfully'
    },
    
    'INVALID_REQUEST': {
        'status': 'error',
        'message': 'Invalid request data',
        'code': 'INVALID_REQUEST'
    },
    
    'INVALID_CREDENTIALS': {
        'status': 'error',
        'message': 'Invalid email or password',
        'code': 'INVALID_CREDENTIALS'
    },
    
    'USER_EXISTS': {
        'status': 'error',
        'message': 'User with this email already exists',
        'code': 'USER_EXISTS'
    },
    
    'USER_NOT_FOUND': {
        'status': 'error',
        'message': 'User not found',
        'code': 'USER_NOT_FOUND'
    },
    
    'UNAUTHORIZED': {
        'status': 'error',
        'message': 'Unauthorized access',
        'code': 'UNAUTHORIZED'
    },
    
    'CREATION_FAILED': {
        'status': 'error',
        'message': 'Failed to create user',
        'code': 'CREATION_FAILED'
    },
    
    'SERVER_ERROR': {
        'status': 'error',
        'message': 'Internal server error',
        'code': 'SERVER_ERROR'
    },
    
    'NOT_FOUND': {
        'status': 'error',
        'message': 'Resource not found',
        'code': 'NOT_FOUND'
    }
}

# HTTP Status Codes
HTTP_STATUS = {
    'OK': 200,
    'CREATED': 201,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'CONFLICT': 409,
    'INTERNAL_SERVER_ERROR': 500
}
