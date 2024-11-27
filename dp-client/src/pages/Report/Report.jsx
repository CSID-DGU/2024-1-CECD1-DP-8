import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useSpring, animated } from '@react-spring/web'; // For smooth animation
import { useDrag } from '@use-gesture/react';
import Spinner from '../../components/Spinner/Spinner';
import styled from 'styled-components';
import { fetchData } from '../../services/api';
import SideBar from '../../components/Report/SideBar';
import PostAnalysisPage from './PostAnalysisPage';
import ReportCard from '../../components/Report/ReportCard';
import HashtagAnalysisPage from './HashtagAnalysisPage';

const influencerIds = [
    1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 14, 16, 17, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 47, 48, 49,
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
];

export default function Report() {
    const { id } = useParams();
    const navigate = useNavigate();

    const [reportData, setReportData] = useState(null);
    const [influencers, setInfluencers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [scrollX, setScrollX] = useState(0);
    const [selectedPage, setSelectedPage] = useState('postAnalysis'); // Default 페이지 설정
    const scrollContainerRef = useRef();

    useEffect(() => {
        const loadReportData = async () => {
            if (id) {
                try {
                    setLoading(true);
                    const data = await fetchData(`/influencer/report/${id}`, { period: 'W' });
                    setReportData(data.result);
                } catch (error) {
                    setError('데이터를 가져오는 중 오류가 발생했습니다.');
                } finally {
                    setLoading(false);
                }
            }
        };
        loadReportData();
    }, [id]);

    useEffect(() => {
        if (!id) {
            const loadInfluencers = async () => {
                try {
                    setLoading(true);
                    const promises = influencerIds.map((id) =>
                        fetchData(`/influencer/report/${id}`, { period: 'W' }).then((res) => ({
                            ...res.result.profile,
                            id,
                        }))
                    );
                    const results = await Promise.all(promises);
                    setInfluencers(results);
                } catch (err) {
                    setError('데이터를 가져오는 중 오류가 발생했습니다.');
                } finally {
                    setLoading(false);
                }
            };
            loadInfluencers();
        }
    }, [id]);

    const [{ x }, setSpring] = useSpring(() => ({
        x: 0,
        config: { tension: 100, friction: 15 },
    }));

    const bind = useDrag((state) => {
        if (state.dragging) {
            setSpring.start({ x: scrollX + state.movement[0] });
        }
        if (state.last) {
            setScrollX((prev) => prev + state.movement[0]);
        }
    });

    useEffect(() => {
        const interval = setInterval(() => {
            if (scrollContainerRef.current) {
                setSpring.start({ x: x.get() - 2 });
                setScrollX((prev) => {
                    if (Math.abs(prev) >= scrollContainerRef.current.scrollWidth / 2) {
                    }
                    return prev - 2;
                });
            }
        }, 20);

        return () => clearInterval(interval);
    }, [x, setSpring]);

    if (loading) return <Spinner />;
    if (error) return <div>{error}</div>;

    if (!id) {
        return (
            <Wrapper>
                <Section>
                    <SectionTitle>다양한 인플루언서들의 리포트를 확인하세요!</SectionTitle>
                    <ScrollableContainer ref={scrollContainerRef}>
                        <AnimatedScroll {...bind()} style={{ x }}>
                            {influencers.concat(influencers).map((profile, idx) => (
                                <CardWrapper key={`${profile.id}-${idx}`}>
                                    <ReportCard profile={profile} />
                                    <Overlay
                                        onClick={(e) => {
                                            e.stopPropagation(); // 이벤트 버블링 방지
                                            navigate(`/report/${profile.id}`);
                                        }}
                                    >
                                        자세히 알아보기 →
                                    </Overlay>
                                </CardWrapper>
                            ))}
                        </AnimatedScroll>
                    </ScrollableContainer>
                </Section>
            </Wrapper>
        );
    }

    if (id && reportData) {
        return (
            <ReportWrapper>
                <SideBar profile={reportData.profile} selectedPage={selectedPage} setSelectedPage={setSelectedPage} />
                <ContentWrapper>
                    {selectedPage === 'postAnalysis' && <PostAnalysisPage reportData={reportData} />}
                    {selectedPage === 'hashtagAnalysis' && <HashtagAnalysisPage id={id} />}
                </ContentWrapper>
            </ReportWrapper>
        );
    }

    return null;
}

const Wrapper = styled.div`
    display: flex;
    max-width: 100%;
    width: 100%;
    margin: 0 auto;
    padding: 0;
    height: 100vh;
    flex-direction: column;
    background: linear-gradient(180deg, #f8fafb 0%, #ffb7f2 100%);

    @media (max-width: 768px) {
        padding: 10px;
        height: auto;
    }
`;

const ReportWrapper = styled.div`
    display: flex;
    max-width: 100%;
    width: 100%;
    margin: 0 auto;
    padding: 20px;

    @media (max-width: 768px) {
        flex-direction: column;
        padding: 10px;
    }
`;

const ContentWrapper = styled.div`
    flex: 1;
    padding: 20px;

    @media (max-width: 768px) {
        padding: 10px;
    }
`;

const Section = styled.div`
    display: flex;
    flex-direction: column;
    padding-top: 20px;
    gap: 20px;

    @media (max-width: 768px) {
        padding-top: 10px;
        gap: 10px;
    }
`;

const SectionTitle = styled.h1`
    font-size: 28px;
    font-weight: 600;
    text-align: center;
    background: linear-gradient(180deg, #d16ba5 0%, #c777b9 50%, #ba83ca 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    @media (max-width: 768px) {
        font-size: 24px;
    }

    @media (max-width: 480px) {
        font-size: 20px;
    }
`;

const ScrollableContainer = styled.div`
    overflow: hidden;
    position: relative;
    width: 100%;
    height: 100%;
    padding: 10px;

    @media (max-width: 768px) {
        padding: 5px;
    }
`;

const AnimatedScroll = styled(animated.div)`
    display: flex;
    gap: 40px;
    will-change: transform;

    @media (max-width: 768px) {
        gap: 20px;
    }

    @media (max-width: 480px) {
        gap: 10px;
    }
`;

const CardWrapper = styled.div`
    cursor: pointer;
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease, opacity 0.3s ease;
    border-radius: 20px;

    &:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);
        opacity: 0.8;
    }

    @media (max-width: 768px) {
        border-radius: 15px;

        &:hover {
            transform: translateY(-5px);
        }
    }

    @media (max-width: 480px) {
        border-radius: 10px;

        &:hover {
            transform: translateY(-3px);
        }
    }
`;

const Overlay = styled.div`
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: white;
    background: rgba(0, 0, 0, 0.6);
    padding: 15px 10px;
    border-radius: 0 0 20px 20px;
    visibility: hidden;

    ${CardWrapper}:hover & {
        visibility: visible;
    }

    @media (max-width: 768px) {
        font-size: 16px;
        padding: 10px 8px;
        border-radius: 0 0 15px 15px;
    }

    @media (max-width: 480px) {
        font-size: 14px;
        padding: 8px 5px;
        border-radius: 0 0 10px 10px;
    }
`;
