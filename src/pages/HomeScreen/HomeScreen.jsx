import {Link, useNavigate } from 'react-router-dom';
import { createRoot } from 'react-dom/client';
import './index.css';
import logo from '../../assets/Logo.png';
import img1 from '../../assets/images/Image(1).jpg'

function HomeScreen() {
  const navigate = useNavigate();
  const handleLogin = () => {
    navigate('/login'),
    navigate('/contact-us')
  };

  return(
  <>
  <section id='nav-bar'>
    <header>
      <h1>Trivamvir</h1>
      <img src={logo}></img>
    </header>
    <div>
      <Link to='/'>Home</Link>
      <Link to='/login'>Login</Link>
      <Link to='/contact-us'>Contact-Us</Link>
    </div>
  </section>
  <section id="main-body">
    <main>
      <article>
        <h1>
          Create.
          <br />
          Connect. 
          <br />
          Play.
        </h1>
      </article>
      <aside>
        <img src={img1} alt="" />
      </aside>
    </main>
    <div>
      <button>Get Started</button>
    </div>
  </section>
  <section id="main-body2">
    <div>
      <h2>Create</h2>
      <p>Come along and create your own <br /> team with exciting new friends</p>
    </div>
    <div>
      <h2>Connect</h2>
      <p>Know the nearest location of <br /> games and tag along with them</p>
    </div>
    <div>
      <h2>Play</h2>
      <p>Play for an endless amount of <br /> time with new community and people</p>
    </div>
  </section>
  </>
  )
}

export default HomeScreen;