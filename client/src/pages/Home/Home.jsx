
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './Home.css';
import Navbar from '../../components/Navbar/Navbar';

function Home() {
  const [user, setUser] = useState('');

  useEffect(() => {
    // Fetch the username from Django
    async function fetchUserInfo() {
      const res = await fetch("/registration/get_user_info/", {
        credentials: "same-origin", // ensure cookies/session are sent
      });

      if (res.ok) {
        const data = await res.json();
        setUser(data); // Set the username state
      } //you could handle the case where theyre not authenticated here and reirect them to sign in page with window.location = "/registration/sign_in/";
    }

    fetchUserInfo();
  }, []);


  return (
    <>
      <Navbar />
      <h1>Home Page</h1>
      <p>Welcome, {user.first_name}!</p>
      <Link to="/profile">Profile</Link>


    </>
  );
}

export default Home;

