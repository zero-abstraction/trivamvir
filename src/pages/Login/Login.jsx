import './index.css';
import {Link, useNavigate} from 'react-router-dom';
import logo from '../../assets/Logo.png';
import { createRoot } from 'react-dom/client';


function Code(){
    return(
        <>
        <div id="login-form-page">
            <h1>Login</h1>
            <a href="/">Back</a>
            <h1>
                Enter the code
            </h1>
            <p>Please enter the valid code send to !phone number!</p>
            <div id="phone">
            <div id="phone-input">
            <input id="number" type="text" name="code" maxlength="6" required></input>
            </div>
            </div>
            <button id='btn2'>Verify</button>
        </div>
        </>
    )
}

function AboutYou(){
    return(
        <>
        <section id="next-steps">
            
        </section>
        </>
    )
}

function CreateAcc(){
    function handler(){
        createRoot(document.getElementById('login-form')).render(
            <Login_Page></Login_Page>
        )
    }
    function handler2(){
        createRoot(document.getElementById('login-form')).render(
            <Code></Code>
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
            <button id='btn2' onClick={handler2}>Send Code</button>
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
    function handler2(){
        createRoot(document.getElementById('login-form')).render(
            <Code></Code>
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
            <button id='btn2' onClick={handler2}>Send Code</button>
        </div>
        </>
    )
}

function Login(){
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
    <div id="LOGIN">
        <header>
            <h1 id="quote">Your Privacy<br /> is our <br />priority</h1>
        </header>
        <div id="login-form">
            <Login_Page></Login_Page>
        </div>
    </div>
    </>
    )
}

export default Login