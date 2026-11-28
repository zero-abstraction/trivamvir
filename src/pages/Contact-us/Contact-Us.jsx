import {Link, useNavigate } from 'react-router-dom';
import { createRoot } from 'react-dom/client';
import './index.css';
import logo from '../../assets/Logo.png';
import img1 from '../../assets/images/Image(1).jpg'

function ContactUs(){
    const navigate = useNavigate();
    const handleLogin = () => {
    navigate('/login')
    };
    return(
    <>
    <section id="nav-bar">
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
    <section id="form">
        <main>
            <h1>Contact Us</h1>
            <textarea placeholder="Type your queries here"></textarea>
            <button>Submit</button>
        </main>
    </section>
    </>
    )
}

export default ContactUs;