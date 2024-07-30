import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Main from './pages/Main/index';
import Advertiser from './pages/Advertiser';
import Influencer from './pages/Influencer';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/advertiser" element={<Advertiser />} />
                <Route path="/influencer" element={<Influencer />} />
            </Routes>
        </Router>
    );
}

export default App;
