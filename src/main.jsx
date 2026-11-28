import { StrictMode } from 'react';
import { createBrowserRouter, RouterProvider, useNavigate } from 'react-router-dom';
import { createRoot } from 'react-dom/client';
import HomeScreen from './pages/HomeScreen/HomeScreen';
import Login from './pages/Login/Login'
import ContactUs from './pages/Contact-us/Contact-Us';



// Create a Browser Router
const router = createBrowserRouter([
  {path: "/", element: <HomeScreen/>},
  {path: "/login", element: <Login />},
  {path: "/contact-us", element: <ContactUs />}
]);


// React code to render directly onto index.html 
createRoot(document.getElementById('root')).render(
  <StrictMode>
  <RouterProvider router={router} />
  </StrictMode>
);
