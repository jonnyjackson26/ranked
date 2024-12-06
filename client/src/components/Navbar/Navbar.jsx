import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Optional: You can style it in a separate CSS file

function Navbar() {
  return (
    <nav className="navbar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/profile">Profile</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;