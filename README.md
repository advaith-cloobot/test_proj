# React App with Flask Backend

A full-stack web application with a React frontend and Flask backend, featuring user authentication and a modern Material Design interface.

## Project Structure

```
test_proj/
├── frontend/                 # React application
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── Login.css
│   │   │   ├── Home.js
│   │   │   └── Home.css
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
├── backend/                  # Flask application
│   ├── constants/
│   │   ├── __init__.py
│   │   └── api_responses.py
│   ├── db_ops/
│   │   ├── __init__.py
│   │   └── user_operations.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── server.py
│   └── requirements.txt
└── README.md
```

## Features

### Frontend (React)
- **Modern UI**: Material Design 3 dark mode interface
- **Responsive Design**: Mobile-friendly layout
- **Routing**: React Router for navigation between pages
- **Components**:
  - Login page with form validation
  - Home dashboard with navigation
  - Material Design icons and typography

### Backend (Flask)
- **RESTful API**: Clean API endpoints for authentication
- **Modular Structure**: Organized into utils, db_ops, and constants
- **CORS Support**: Cross-origin resource sharing enabled
- **Error Handling**: Consistent API response format

## Getting Started

### Prerequisites
- Node.js (v14 or higher)
- Python 3.7 or higher
- pip (Python package manager)

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The React app will be available at `http://localhost:3000`

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the Flask server:
```bash
python server.py
```

The Flask API will be available at `http://localhost:5000`

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `GET /api/user/profile` - Get user profile

### Health Check
- `GET /` - Server health check

## Design System

The application follows Google Material Design 3 principles with a dark mode theme:

### Colors
- **Background**: #0D0D0D (Color 1)
- **Surface**: #1A1A1A (Color 2)
- **Cards**: #262626 (Color 3)
- **Accent**: #C82FFF (Magenta)
- **Gradient**: Linear gradient from #C82FFF to #00AAFF
- **Text**: #FFFFFF (White)
- **Placeholder**: #A8A8A8

### Typography
- **Font Family**: Montserrat (Regular, Medium, Semi-bold)
- **Icons**: Material Symbols (weight: 200, fill: off)

## Development Notes

- The backend uses in-memory storage for demo purposes
- In production, replace with a proper database (PostgreSQL, MySQL, etc.)
- Implement proper JWT authentication for production use
- Add input validation and sanitization
- Implement proper error logging and monitoring

## License

This project is for educational and demonstration purposes.