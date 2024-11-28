import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store/store';
import Main from './pages/Main/index';
import Advertiser from './pages/Advertiser';
import Influencer from './pages/Influencer';
import InfluencerMypage from './pages/Mypage/InfluencerMypage';
import Report from './pages/Report/Report';
import AdvertiserMypage from './pages/Mypage/AdvertiserMypage';
import SignUp from './pages/Signup/Signup';
import Footer from './components/Footer/Footer';
import RecommendPage from './pages/Recommend/RecommendPage';
import Chat from './pages/Recommend/Chat';
import KakaoRedirect from './pages/Login/Redirect';
import Navbar from './components/Navbar/Navbar';
import Spinner from './components/Spinner/Spinner';
import NotFound from './pages/NotFound/NotFound';

function App() {
    const [loading, setLoading] = useState(false);

    // Simulating loading for demonstration purposes
    useEffect(() => {
        setLoading(true);
        const timer = setTimeout(() => setLoading(false), 1000);
        return () => clearTimeout(timer);
    }, []);

    return (
        <Provider store={store}>
            <Router>
                {loading && <Spinner />}
                <Navbar />
                <Routes>
                    <Route path="/" element={<Main />} />
                    <Route path="/advertiser" element={<Advertiser />} />
                    <Route path="/influencer" element={<Influencer />} />
                    <Route path="/report/:id" element={<Report />} />
                    <Route path="/report" element={<Report />} />
                    <Route path="/influmypage" element={<InfluencerMypage />} />
                    <Route path="/admypage" element={<AdvertiserMypage />} />
                    <Route path="/signup" element={<SignUp />} />
                    <Route path="/recommend" element={<RecommendPage />} />
                    <Route path="/chat" element={<Chat />} />
                    <Route path="/oauth" element={<KakaoRedirect />} />
                    <Route path="*" element={<NotFound />} />
                </Routes>
                <Footer />
            </Router>
        </Provider>
    );
}

export default App;
