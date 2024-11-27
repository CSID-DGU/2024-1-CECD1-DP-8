import React, { useState } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import FilterIcon from '../../assets/filter-add.svg';
import SearchIcon from '../../assets/search-icon.png';
import InfluencerFilterModal from '../../components/Filter/InfluencerFilterModal';
import Spinner from '../../components/Spinner/Spinner';
import { fetchChatResponse } from '../../services/chatApi';
export default function RecommendPage() {
    const [showModal, setShowModal] = useState(false);
    const [searchPrompt, setSearchPrompt] = useState('');
    const [loading, setLoading] = useState(false);
    const [filters, setFilters] = useState({
        beauty: false,
        fashion: false,
        sports: false,
        minFollower: 0,
        maxFollower: 0,
        minImpactScore: 0,
        maxImpactScore: 0,
        gender: 'unset',
        hashtagInput: '',
    });

    const navigate = useNavigate();

    const handleOpenModal = () => setShowModal(true);
    const handleCloseModal = () => setShowModal(false);

    const handleSearch = async () => {
        if (searchPrompt.trim() === '') {
            alert('검색어를 입력해주세요!');
            return;
        }

        setLoading(true); // 로딩 시작
        try {
            // fetchChatResponse를 호출
            const data = await fetchChatResponse(searchPrompt);

            // 검색 결과를 Chat 페이지로 전달
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
            setLoading(false); // 로딩 종료
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSearch();
        }
    };

    return (
        <PageWrapper>
            {loading && <Spinner />}
            <Container>
                <MainContent>
                    <Title>원하는 인플루언서를 쉽고 편하게 찾아보세요!</Title>
                    <Subtitle>
                        생성형 AI를 통해 원하는 인플루언서를 특징이나 키워드 검색을 통해 추천받아보세요.
                    </Subtitle>
                    <SearchContainer>
                        <SearchInput
                            placeholder="원하는 인플루언서를 검색해보세요"
                            value={searchPrompt}
                            onChange={(e) => setSearchPrompt(e.target.value)}
                            onKeyPress={handleKeyPress}
                        />
                        <SearchIconContainer onClick={handleSearch}>
                            <StyledSearchIcon src={SearchIcon} alt="Search Icon" />
                        </SearchIconContainer>
                    </SearchContainer>
                    <Description>
                        검색이 완료되면 원하는 인플루언서가 추천되고, 생성형 AI에게 자세히 물어볼 수 있어요.
                    </Description>
                    <KeywordButton onClick={handleOpenModal}>
                        필터 & 키워드 검색
                        <StyledFilterIcon src={FilterIcon} alt="Search Icon" />
                    </KeywordButton>
                </MainContent>
            </Container>

            {showModal && (
                <InfluencerFilterModal
                    setModalOpen={setShowModal}
                    filters={filters}
                    setFilters={setFilters}
                    setSearchPrompt={setSearchPrompt}
                />
            )}
        </PageWrapper>
    );
}
const PageWrapper = styled.div`
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    background: linear-gradient(180deg, #f8fafb 0%, #ade3fe 100%);
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);

    @media (max-width: 768px) {
        height: auto;
        padding: 20px;
    }
`;

const Container = styled.div`
    width: 100%;
    max-width: 1200px;
    padding: 20px;

    @media (max-width: 768px) {
        padding: 10px;
    }
`;

const MainContent = styled.div`
    margin-top: 100px;
    text-align: center;

    @media (max-width: 768px) {
        margin-top: 50px;
    }
`;

const Title = styled.h2`
    background: linear-gradient(180deg, #4017e3 0%, #230d7d 83%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: Inter;
    font-size: 48px;
    font-weight: 600;
    line-height: normal;

    @media (max-width: 768px) {
        font-size: 36px;
    }

    @media (max-width: 480px) {
        font-size: 28px;
    }
`;

const Subtitle = styled.p`
    background: linear-gradient(180deg, #780bc2 0%, #39055c 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 20px;
    margin-top: 10px;

    @media (max-width: 768px) {
        font-size: 18px;
    }

    @media (max-width: 480px) {
        font-size: 16px;
    }
`;

const StyledSearchIcon = styled.img`
    width: 19px;
    height: 19px;
    cursor: pointer;

    @media (max-width: 480px) {
        width: 16px;
        height: 16px;
    }
`;

const StyledFilterIcon = styled.img`
    width: 24px;
    height: 24px;
    margin-left: 3px;

    @media (max-width: 480px) {
        width: 20px;
        height: 20px;
    }
`;

const SearchContainer = styled.div`
    position: relative;
    margin: 40px auto;
    width: 60%;

    @media (max-width: 768px) {
        width: 80%;
    }

    @media (max-width: 480px) {
        width: 90%;
    }
`;

const SearchInput = styled.input`
    width: 100%;
    padding: 15px 20px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 50px;

    @media (max-width: 480px) {
        padding: 12px 15px;
        font-size: 14px;
    }
`;

const SearchIconContainer = styled.div`
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;

    @media (max-width: 480px) {
        right: 15px;
    }
`;

const KeywordSection = styled.div`
    margin: 20px auto;
    text-align: center;

    @media (max-width: 480px) {
        margin: 10px auto;
    }
`;

const KeywordInput = styled.input`
    width: 60%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 30px;
    font-size: 16px;

    @media (max-width: 768px) {
        width: 80%;
    }

    @media (max-width: 480px) {
        width: 90%;
        padding: 10px;
        font-size: 14px;
    }
`;

const KeywordDescription = styled.p`
    margin-top: 10px;
    font-size: 14px;
    color: #666;

    @media (max-width: 480px) {
        font-size: 12px;
    }
`;

const Description = styled.p`
    color: #8c8c8c;
    text-align: center;
    font-family: Inter;
    font-size: 20px;
    font-weight: 600;

    @media (max-width: 768px) {
        font-size: 18px;
    }

    @media (max-width: 480px) {
        font-size: 16px;
    }
`;

const KeywordButton = styled.button`
    background: #8a54ff;
    border: none;
    height: 50px;
    padding: 5px 15px 5px 20px;
    border-radius: 30px;
    background: linear-gradient(90deg, #aa96fc 0%, #463392 100%);
    box-shadow: 0px 3px 3px 0px rgba(0, 0, 0, 0.25);
    color: white;
    cursor: pointer;
    margin-top: 20px;
    font-size: 20px;

    &:hover {
        background: #6a40cc;
    }

    @media (max-width: 768px) {
        font-size: 18px;
        padding: 10px 15px;
    }

    @media (max-width: 480px) {
        font-size: 16px;
        padding: 8px 12px;
    }
`;
