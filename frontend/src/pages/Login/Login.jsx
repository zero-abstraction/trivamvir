import './index.css';
import {Link, useNavigate} from 'react-router-dom';
import logo from '../../assets/Logo.png';
import { createRoot } from 'react-dom/client';


function CreateAcc(){
    function handler(){
        createRoot(document.getElementById('login-form')).render(
            <Login_Page></Login_Page>
        )
    }
    return(
        <>
        <div id="login-form-page">
            <h1>Create Account</h1>
            <a href="/">Back</a>
            <h1>
                What's your 
                <br></br>
                number?
            </h1>
            <p>We'll text you a 6 digit code. A verified phone number is required to join games</p>
            <p>Phone number</p>
            <div id="phone">
            <div id="phone-input">
            <select id='number-code'>
                <option value="+91">+91</option>
            </select>
            <input id="number" type="tel" name="phone" maxlength="10" pattern="[0-9]{10}" onInput={(e) => {
                e.target.value = e.target.value.replace(/[^0-9]/g, '');
            }} required></input>
            </div>
            <div id='phone-redirect'>
            <p>Already have an account?</p>
            <button id='btn1' onClick={handler}>Log in</button>
            </div>
            </div>
            <button id='btn2'>Send Code</button>
        </div>
        </>
    )
}


function Login_Page(){
    function handler(){
     createRoot(document.getElementById('login-form')).render(
        <CreateAcc></CreateAcc>
     )
    }
    return(
        <>
        <div id="login-form-page">
            <h1>Login</h1>
            <a href="/">Back</a>
            <h1>
                What's your 
                <br></br>
                number?
            </h1>
            <p>We'll text you a 6 digit code. A verified phone number is required to join games</p>
            <p>Phone number</p>
            <div id="phone">
            <div id="phone-input">
            <select id='number-code'>
                <option value="+91">+91</option>
            </select>
            <input id="number" type="tel" name="phone" maxlength="10" pattern="[0-9]{10}" onInput={(e) => {
                e.target.value = e.target.value.replace(/[^0-9]/g, '');
            }} required></input>
            </div>
            <div id='phone-redirect'>
            <p>Don't have an account?</p>
            <button id='btn1' onClick={handler}>Create One</button>
            </div>
            </div>
            <button id='btn2'>Send Code</button>
        </div>
        </>
    )
}

function Login(){
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
    <div id="LOGIN">
        <h1 id="quote">Your Privacy <br></br>  is our <br></br> priority</h1>
    <div id="login-form">
        <Login_Page></Login_Page>
    </div>
    </div>
    </>
    )
}

export default Login