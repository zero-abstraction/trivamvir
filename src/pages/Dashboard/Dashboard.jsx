import './index.css';
import {Link, useNavigate} from 'react-router-dom';
import logo from '../../assets/Logo.png';
import { createRoot } from 'react-dom/client';

function dashboard(){
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
              <Link>Contact-Us</Link>
            </div>
          </section>
          
        </>
    )
}

export default dashboard;