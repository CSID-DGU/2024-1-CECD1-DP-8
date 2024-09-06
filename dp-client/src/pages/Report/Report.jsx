import React, { useState } from 'react';
import SideBar from '../../components/Report/SideBar';
import FollowerTrendPage from './FollowerTrendPage';
import data from './data.json';
import InfluencerNavbar from '../../components/Navbar/InfluencerNavbar';
import PostAnalysisPage from './PostAnalysisPage';
import ReelsAnalysisPage from './ReelsAnalysisPage';
import SimilarInfluencerPage from './SimilarInfluencerPage';
import styled from 'styled-components';
export default function Report() {
    const [selectedPage, setSelectedPage] = useState('postAnalysis');

    const renderPage = () => {
        switch (selectedPage) {
            case 'postAnalysis':
                return <PostAnalysisPage />;
            case 'followerTrend':
                return <FollowerTrendPage />;
            default:
                return <SimilarInfluencerPage />;
        }
    };

    return (
        <div>
            <Wrapper>
                <SideBar profile={data.result.profile} onSelect={setSelectedPage} />
                {renderPage()}
            </Wrapper>
        </div>
    );
}

const Wrapper = styled.div`
    display: flex;
    max-width: 1400px; // 레이아웃을 중앙으로 맞추기 위해 최대 너비를 지정
    margin: 0 auto;
    background: #f5f5f5;
`;
