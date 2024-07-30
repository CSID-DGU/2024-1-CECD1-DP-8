import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Main from './pages/Main/index';
import Advertiser from './pages/Advertiser';
import Influencer from './pages/Influencer';
import MatchingPage from './pages/Advertiser/MatchingPage';
import InfluencerMypage from './pages/Mypage/InfluencerMypage';
import Report from './pages/Influencer/Report';
import AdvertiserMypage from './pages/Mypage/AdvertiserMypage';
import GlobalStyle from './styles/GlobalStyle';

function App() {
    return (
        <Router>
            <GlobalStyle />
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/advertiser" element={<Advertiser />} />
                <Route path="/influencer" element={<Influencer />} />
                <Route path="/report" element={<Report />} />
                <Route path="/influmypage" element={<InfluencerMypage />} />
                <Route path="/admypage" element={<AdvertiserMypage />} />
                <Route path="/matchingPage" element={<MatchingPage />} />
                <Route
                    path="/*"
                    element={
                        <div>
                            <h2>이 페이지는 존재하지 않습니다</h2>
                        </div>
                    }
                />
            </Routes>
        </Router>
    );
}

export default App;
