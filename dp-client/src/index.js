import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import GlobalStyles from './styles/GlobalStyle';
import { Provider } from 'react-redux';
import AdvertiserNavbar from './components/Navbar/AdvertiserNavbar';
import InfluencerNavbar from './components/Navbar/InfluencerNavbar';
import Footer from './components/Footer/Footer';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <GlobalStyles />
        <App />
    </React.StrictMode>
);
