import {Link, useNavigate } from 'react-router-dom';
import { createRoot } from 'react-dom/client';
import './index.css';
import logo from '../../assets/Logo.png';


function HomeScreen() {
  const navigate = useNavigate();
  const handleLogin = () => {
    navigate('/login')
  };

  return(
  <>
  <div id="navBar">
    <div id="logo">
    <img src={logo} alt="Logo" />
    <h1>Trivamvir</h1>
    </div>
    <div id="navigate">
        <Link to="/">Home</Link>
        <Link to="/why-us">Why us?</Link>
        <Link to="/contact-us">Contact us</Link>
        <Link to="/login">Log in</Link>
    </div>
  </div>
  <div id="headers">
    <div id="head">
      <h1>Connect. <br></br> Belong. <br></br> Thrive.</h1>
    </div>
    <div id="card">
    <div id="cards">
     <img src="src/assets/images/image(1).jpg" alt="image"/>
     <img src="src/assets/images/image(2).jpg" alt="image"/>
     <img src="src/assets/images/image(3).jpg" alt="image"/>
    </div>
  </div>
  </div>
  <button id="redirect" onClick={handleLogin}>Get Started</button>
  </>
  )
}

export default HomeScreen;