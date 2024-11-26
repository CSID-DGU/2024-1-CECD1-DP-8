import React, { useState } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import FilterIcon from '../../assets/filter-add.svg';
import SearchIcon from '../../assets/search-icon.png';
import InfluencerFilterModal from '../../components/Filter/InfluencerFilterModal';
import Spinner from '../../components/Spinner/Spinner';
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
            const response = await fetch('https://4e4e-34-87-133-241.ngrok-free.app/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: searchPrompt }),
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
                <InfluencerFilterModal setModalOpen={setShowModal} filters={filters} setFilters={setFilters} />
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
`;

const Container = styled.div`
    width: 100%;
    max-width: 1200px;
    padding: 20px;
`;

const MainContent = styled.div`
    margin-top: 100px;
    text-align: center;
`;

const Title = styled.h2`
    background: linear-gradient(180deg, #4017e3 0%, #230d7d 83%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: Inter;
    font-size: 48px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
`;

const Subtitle = styled.p`
    background: linear-gradient(180deg, #780bc2 0%, #39055c 100%);
    background-clip: text;
    margin-top: 10px;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
`;

const StyledSearchIcon = styled.img`
    width: 19px;
    height: 19px;
    flex-shrink: 0;
    cursor: pointer;
`;

const StyledFilterIcon = styled.img`
    width: 24px;
    height: 24px;
    color: #fff;
    margin-left: 3px;
`;

const SearchContainer = styled.div`
    position: relative;
    margin: 40px auto;
    width: 60%;
`;

const SearchInput = styled.input`
    width: 100%;
    padding: 15px 20px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 50px;
`;

const SearchIconContainer = styled.div`
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    color: #666;
    cursor: pointer;
`;

const KeywordSection = styled.div`
    margin: 20px auto;
    text-align: center;
`;

const KeywordInput = styled.input`
    width: 60%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 30px;
    font-size: 16px;
    outline: none;
`;

const KeywordDescription = styled.p`
    margin-top: 10px;
    font-size: 14px;
    color: #666;
`;

const Description = styled.p`
    color: #8c8c8c;
    text-align: center;
    font-family: Inter;
    font-size: 20px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
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
`;
