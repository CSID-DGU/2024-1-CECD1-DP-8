import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation, useNavigate } from 'react-router-dom';
import Main from './pages/Main/index';
import Advertiser from './pages/Advertiser';
import Influencer from './pages/Influencer';
import MatchingPage from './pages/Advertiser/MatchingPage';
import InfluencerMypage from './pages/Mypage/InfluencerMypage';
import Report from './pages/Report/Report';
import AdvertiserMypage from './pages/Mypage/AdvertiserMypage';
import MatchingPage2 from './pages/Advertiser/MatchingPage2';
import SignUp from './pages/Signup/Signup';
import { NavbarProvider, useNavbar } from './store/NavbarContext';
import AdvertiserNavbar from './components/Navbar/AdvertiserNavbar';
import InfluencerNavbar from './components/Navbar/InfluencerNavbar';

function App() {
    return (
        <NavbarProvider>
            <Router>
                <NavbarRenderer /> {/* Navbar 렌더링 */}
                <ResetNavbarOnMain />
                <Routes>
                    <Route path="/" element={<Main />} />
                    <Route path="/advertiser" element={<Advertiser />} />
                    <Route path="/influencer" element={<Influencer />} />
                    <Route path="/report" element={<Report />} />
                    <Route path="/influmypage" element={<InfluencerMypage />} />
                    <Route path="/admypage" element={<AdvertiserMypage />} />
                    <Route path="/matchingPage" element={<MatchingPage />} />
                    <Route path="/matchingPage2" element={<MatchingPage2 />} />
                    <Route path="/signup" element={<SignUp />} />
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
        </NavbarProvider>
    );
}

export default App;

// Navbar를 렌더링하는 컴포넌트
function NavbarRenderer() {
    const { navbar } = useNavbar();

    if (navbar === 'advertiser') {
        return <AdvertiserNavbar />;
    } else if (navbar === 'influencer') {
        return <InfluencerNavbar />;
    } else {
        return null;
    }
}

// 메인 페이지로 돌아갈 때 Navbar를 초기화하는 컴포넌트
function ResetNavbarOnMain() {
    const { setNavbar } = useNavbar();
    const location = useLocation();
    const navigate = useNavigate();

    useEffect(() => {
        // 메인 페이지('/')로 돌아갈 때 Navbar 상태 초기화
        if (location.pathname === '/') {
            setNavbar(null);
        }
    }, [location, setNavbar]);

    return null;
}
