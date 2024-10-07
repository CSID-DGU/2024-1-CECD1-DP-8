import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom'; // useParams를 이용해 id를 가져옴
import SideBar from '../../components/Report/SideBar';
import styled from 'styled-components';
import { fetchData } from '../../services/api';
import PostAnalysisPage from './PostAnalysisPage';
import FollowerTrendPage from './FollowerTrendPage';
import SimilarInfluencerPage from './SimilarInfluencerPage';

export default function Report() {
    const { id } = useParams(); // URL에서 id 파라미터를 받아옴
    const [selectedPage, setSelectedPage] = useState('postAnalysis');
    const [reportData, setReportData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // API 호출 및 데이터 저장
    useEffect(() => {
        const loadReportData = async () => {
            try {
                const data = await fetchData(`/influencer/report/${id}`, { period: 'W' });
                setReportData(data.result);
            } catch (error) {
                setError('데이터를 가져오는 중 오류가 발생했습니다.');
            } finally {
                setLoading(false);
            }
        };
        loadReportData();
    }, [id]);

    if (loading) return <div>로딩 중...</div>;
    if (error) return <div>{error}</div>;
    if (!reportData) return <div>데이터가 없습니다.</div>;

    const renderPage = () => {
        switch (selectedPage) {
            case 'postAnalysis':
                return <PostAnalysisPage reportData={reportData} />;
            case 'followerTrend':
                return <FollowerTrendPage reportData={reportData} />;
            case 'similarInfluencer':
                return <SimilarInfluencerPage reportData={reportData} />;
            default:
                return <PostAnalysisPage reportData={reportData} />;
        }
    };

    return (
        <Wrapper>
            <SideBar profile={reportData.profile} onSelect={setSelectedPage} />
            <ContentWrapper>{renderPage()}</ContentWrapper>
        </Wrapper>
    );
}

const Wrapper = styled.div`
    display: flex;
    max-width: 1800px;
    width: 100vw;
    min-width: 1400px;
    margin: 0 auto;
`;

const ContentWrapper = styled.div`
    flex: 1;
    padding: 20px;
`;