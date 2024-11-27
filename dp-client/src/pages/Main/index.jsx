import React, { useState, useEffect, useRef } from 'react';
import { useSpring, animated } from '@react-spring/web'; // For smooth animation
import { useDrag } from '@use-gesture/react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import InstaIcon from '../../assets/instaicon.svg';
import Spinner from '../../components/Spinner/Spinner';
import FilterIcon from '../../assets/filter-add.svg';
import SearchIcon from '../../assets/search-icon.png';
import InfluencerFilterModal from '../../components/Filter/InfluencerFilterModal';
import AdvertiserMain from '../Advertiser/index';
import InfluencerMain from '../Influencer/index';
const imagePaths = Array.from({ length: 18 }, (_, i) => require(`../../assets/influimg/influ_${i + 1}.png`));

export default function Main() {
    const [showFilterModal, setShowFilterModal] = useState(false);
    const [searchPrompt, setSearchPrompt] = useState('');
    const navigate = useNavigate();
    const [scrollX, setScrollX] = useState(0);
    const scrollContainerRef = useRef();
    const [loading, setLoading] = useState(false);
    const [filters, setFilters] = useState({
        selectedCategory: null,
        minFollower: '',
        maxFollower: '',
        gender: 'unset',
        hashtagInput: '',
    });

    const handleOpenFilterModal = () => {
        setShowFilterModal(true);
    };

    const handleCloseFilterModal = () => {
        setShowFilterModal(false);
    };

    const handleSearch = async () => {
        if (searchPrompt.trim() === '') {
            alert('검색어를 입력해주세요!');
            return;
        }

        setLoading(true); // 로딩 시작
        try {
            const response = await fetch('https://8c49-104-196-152-227.ngrok-free.app/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    question: searchPrompt,
                    filters: {
                        ...(filters.selectedCategory && { category: filters.selectedCategory }),
                        ...(filters.minFollower && { minFollower: filters.minFollower }),
                        ...(filters.maxFollower && { maxFollower: filters.maxFollower }),
                        ...(filters.gender !== 'unset' && { gender: filters.gender }),
                        ...(filters.hashtagInput && { tag: filters.hashtagInput.split(' ') }),
                    },
                }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();

            navigate('/chat', {
                state: {
                    question: searchPrompt,
                    chatResponse: data.result,
                },
            });
        } catch (err) {
            console.error('API 호출 오류:', err);
            alert('서버와 연결할 수 없습니다. 다시 시도해주세요.');
        } finally {
            setLoading(false);
        }
    };

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
                        return 0;
                    }
                    return prev - 2;
                });
            }
        }, 20);

        return () => clearInterval(interval);
    }, [x, setSpring]);

    return (
        <Wrapper>
            {loading && <Spinner />}
            <BlurBackground />
            <Content>
                <IconWrapper>
                    <img src={InstaIcon} alt="Insta Icon" />
                </IconWrapper>
                <Title>
                    <span>원하는 인플루언서를 추천 받아보세요</span>
                </Title>
                <Subtitle>
                    <span>AI 기반 검색과</span> <span>맞춤 추천을 경험하세요</span>
                </Subtitle>
                <SearchContainer>
                    <SearchInput
                        placeholder="예: 팔로워 1만 이상의 여성 뷰티 인플루언서를 추천해줘"
                        value={searchPrompt}
                        onChange={(e) => setSearchPrompt(e.target.value)}
                        onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
                    />
                    <SearchIconContainer onClick={handleSearch}>
                        <StyledSearchIcon src={SearchIcon} alt="Search Icon" />
                    </SearchIconContainer>
                </SearchContainer>
                <KeywordButton onClick={handleOpenFilterModal}>
                    필터 & 키워드 검색
                    <StyledFilterIcon src={FilterIcon} alt="Search Icon" />
                </KeywordButton>
            </Content>
            <InfluencerTitle>
                <span>다양한 인플루언서들과 함께하세요</span>
            </InfluencerTitle>
            <InfiniteScrollContainer ref={scrollContainerRef}>
                <AnimatedScroll {...bind()} style={{ x }}>
                    {imagePaths.concat(imagePaths).map((src, idx) => (
                        <Card key={idx}>
                            <Image src={src} alt={`Influencer ${idx + 1}`} />
                        </Card>
                    ))}
                </AnimatedScroll>
            </InfiniteScrollContainer>
            {showFilterModal && (
                <InfluencerFilterModal
                    setModalOpen={setShowFilterModal}
                    filters={filters}
                    setFilters={setFilters}
                    setSearchPrompt={setSearchPrompt}
                />
            )}
            <Section>
                <AdvertiserMain />
            </Section>
            <Section>
                <InfluencerMain />
            </Section>
        </Wrapper>
    );
}

const Wrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    overflow-x: hidden;
    position: relative;
`;

const BlurBackground = styled.div`
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(
        circle at 30% 50%,
        rgba(255, 182, 193, 0.4) 0%,
        rgba(88, 101, 242, 0.4) 60%,
        rgba(255, 255, 255, 0) 90%
    );
    filter: blur(70px);
    z-index: -1;
`;

const Content = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 20px;
    max-width: 800px;

    @media (max-width: 768px) {
        max-width: 90%;
    }
`;

const IconWrapper = styled.div`
    width: 100px;
    height: 100px;
    margin-bottom: 20px;

    img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: drop-shadow(0px 8px 15px rgba(0, 0, 0, 0.2));
    }
`;

const Title = styled.h1`
    font-size: 2.5rem;
    font-family: 'Helvetica Neue', sans-serif;
    font-weight: bold;
    color: #1c1c1c;
    margin-bottom: 10px;
    line-height: 1.2;
    background: linear-gradient(90deg, #ff7eb3 0%, #7854f7 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    span {
        display: block;
    }

    @media (max-width: 768px) {
        font-size: 1.8rem;
    }
`;

const Subtitle = styled.h2`
    font-size: 1.2rem;
    font-family: 'Helvetica Neue', sans-serif;
    font-weight: 400;
    color: #666;
    margin-bottom: 30px;
    line-height: 1.5;

    @media (max-width: 768px) {
        font-size: 1rem;
    }
`;

const SearchContainer = styled.div`
    position: relative;
    margin: 20px auto;
    width: 800px;
    @media (max-width: 768px) {
        width: 100%;
    }
`;

const SearchInput = styled.input`
    width: 100%;
    padding: 15px 20px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 50px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
`;

const SearchIconContainer = styled.div`
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
`;

const StyledSearchIcon = styled.img`
    width: 24px;
    height: 24px;
`;

const KeywordButton = styled.button`
    margin-top: 20px;
    padding: 12px 24px;
    border-radius: 30px;
    background: linear-gradient(90deg, #aa96fc 0%, #463392 100%);
    color: #fff;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;

    &:hover {
        background: #6a40cc;
    }

    @media (max-width: 768px) {
        padding: 10px 20px;
    }
`;

const StyledFilterIcon = styled.img`
    width: 20px;
    height: 20px;
`;

const InfluencerTitle = styled.div`
    margin-top: 2rem;
    font-size: 2rem;
    font-family: 'Helvetica Neue', sans-serif;
    font-weight: 500;
    color: #1c1c1c;
    margin-bottom: 2rem;
    line-height: 1.2;
    background: linear-gradient(90deg, #ff6f91 0%, #ff9671 40%, #ffc75f 70%, #ffa07a 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    span {
        display: block;
    }

    @media (max-width: 768px) {
        font-size: 1.8rem;
    }
`;

const InfiniteScrollContainer = styled.div`
    width: 100%;
    position: relative;
`;

const AnimatedScroll = styled(animated.div)`
    display: flex;
    gap: 40px;
`;

const Card = styled.div`
    flex: none;
    cursor: pointer;
    transition: transform 0.3s ease;
    &:hover {
        transform: scale(1.1);
    }
`;

const Image = styled.img`
    object-fit: cover;
    width: 230px;
    border-radius: 20px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
`;

const Section = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    padding: 50px 0;
    background: transparent;
    margin-top: 20px;

    @media (max-width: 768px) {
        padding: 30px 10px;
    }
`;
