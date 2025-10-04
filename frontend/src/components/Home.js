import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    navigate('/login');
  };

  return (
    <div className="home-container">
      <nav className="home-nav">
        <div className="nav-content">
          <h1 className="nav-title">Dashboard</h1>
          <button onClick={handleLogout} className="logout-button">
            <span className="material-symbols-outlined">logout</span>
            Logout
          </button>
        </div>
      </nav>
      
      <main className="home-main">
        <div className="welcome-section">
          <h2 className="welcome-title">Welcome to your Dashboard</h2>
          <p className="welcome-subtitle">
            You have successfully logged in. This is your home page.
          </p>
        </div>
        
        <div className="cards-grid">
          <div className="info-card">
            <div className="card-icon">
              <span className="material-symbols-outlined">dashboard</span>
            </div>
            <h3 className="card-title">Dashboard</h3>
            <p className="card-description">
              View your analytics and key metrics in one place.
            </p>
          </div>
          
          <div className="info-card">
            <div className="card-icon">
              <span className="material-symbols-outlined">settings</span>
            </div>
            <h3 className="card-title">Settings</h3>
            <p className="card-description">
              Manage your account settings and preferences.
            </p>
          </div>
          
          <div className="info-card">
            <div className="card-icon">
              <span className="material-symbols-outlined">notifications</span>
            </div>
            <h3 className="card-title">Notifications</h3>
            <p className="card-description">
              Stay updated with the latest news and alerts.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
