import { useState, useEffect } from 'react'
import './ProfilePage.css'
import { Link } from 'react-router-dom';
import Navbar from '../../components/Navbar/Navbar';
function ProfilePage() {
    const [user, setUser] = useState('');
    const [physicalAttributes, setPhysicalAttributes] = useState(null);

    useEffect(() => {
      // Fetch the username and physical attributes from Django
      async function fetchUserInfo() {
          const res = await fetch("/registration/get_user_info/", {
              credentials: "same-origin", // ensure cookies/session are sent
          });

          if (res.ok) {
              const data = await res.json();
              setUser(data); // Set the username state
          }
      }

      async function fetchPhysicalAttributes() {
          const res = await fetch("/get-physical-attributes/", {
              credentials: "same-origin", // ensure cookies/session are sent
          });

          if (res.ok) {
              const data = await res.json();
              setPhysicalAttributes(data); // Set physical attributes state
          }
      }

      fetchUserInfo();
      fetchPhysicalAttributes();
  }, []);

  async function logout() {
    const res = await fetch("/registration/logout/", {
      credentials: "same-origin", // include cookies!
    });

    if (res.ok) {
      // navigate away from the single page app!
      window.location = "/registration/sign_in/";
    } else {
      // handle logout failed!
    }
  }

  return (
    <>
      <Navbar />
      <h1>Profile Page</h1>
      <p>username: {user.username}</p>
      <p>first_name: {user.first_name}</p>
      <p>last_name: {user.last_name}</p>
      <p>email: {user.email}</p>
      <p>date_joined: {user.date_joined}</p>
      <Link to="/">Home</Link>
      <button onClick={logout}>Logout</button>



      <h2>Physical Attributes</h2>
            {physicalAttributes ? (
                <div>
                    <p>Height: {physicalAttributes.height} inches</p>
                    <p>Weight: {physicalAttributes.weight} lbs</p>
                    <p>Fastest 40-yard dash: {physicalAttributes.fastest_40_yard_dash} seconds</p>
                    <p>Bench Press Max: {physicalAttributes.bench_press_max} lbs</p>
                    <p>Deadlift Max: {physicalAttributes.deadlift_max} lbs</p>
                    <p>Squat Max: {physicalAttributes.squat_max} lbs</p>
                    <p>Wingspan: {physicalAttributes.wingspan} inches</p>
                    <p>Vertical Jump Height: {physicalAttributes.vertical_jump_height} inches</p>
                    <p>Resting Heart Rate: {physicalAttributes.resting_heart_rate} bpm</p>
                    <p>VO2 Max: {physicalAttributes.vo2_max}</p>
                    <p>Dominant Hand: {physicalAttributes.dominant_hand}</p>
                    <p>Eye Color: {physicalAttributes.eye_color}</p>
                    <p>Hair Color: {physicalAttributes.hair_color}</p>
                </div>
            ) : (
                <p>Loading physical attributes...</p>
            )}


    </>
  )
}

export default ProfilePage;

