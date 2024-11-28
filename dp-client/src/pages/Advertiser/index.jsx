import React from 'react';
import AdvertiserNavbar from '../../components/Navbar/AdvertiserNavbar';
import { styled } from 'styled-components';
import { Link } from 'react-router-dom';

export default function AdvertiserMain() {
    return (
        <>
            <Wrapper>
                <IntroWrapper>
                    <a>인플루언서 추천</a>
                    <h1>
                        원하는 인플루언서를 <br />
                        AI에게 물어보세요!
                    </h1>
                </IntroWrapper>
                <StyledLink to="/recommend">
                    <SearchButton>인플루언서 추천 받기</SearchButton>
                </StyledLink>
                <HomepageSection>
                    <h2>AI 모델에게 인플루언서를 추천 받으세요.</h2>
                    <p>
                        고객님의 원하는 인플루언서의 요구사항을 포함하여, 카테고리 (관심 분야), 팔로워수, 성별, 해시태그
                        등을 선택하세요. 해당 조건에 맞춰 원하는 인플루언서 리스트를 바로 확인할 수 있습니다.
                    </p>
                    <img src={require('../../assets/adintro.png')} alt="홈페이지 스크린샷" />
                </HomepageSection>
            </Wrapper>
        </>
    );
}

const Wrapper = styled.div`
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 0 20px;
`;

const IntroWrapper = styled.div`
    display: flex;
    margin-top: 5rem;
    width: 660px;
    height: auto;
    flex-direction: column;
    text-align: center;

    a {
        color: #780bc2;
        font-family: Inter, sans-serif;
        font-size: 25px;
        font-weight: 600;
        background: linear-gradient(180deg, #780bc2 0%, #39055c 100%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    h1 {
        background: linear-gradient(180deg, #4017e3 0%, #230d7d 83%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: Inter, sans-serif;
        font-size: 48px;
        font-weight: 600;
        line-height: 1.2;
        margin-top: 1rem;
    }

    @media (max-width: 768px) {
        width: 100%;
        a {
            font-size: 20px;
        }

        h1 {
            font-size: 32px;
        }
    }
`;

const StyledLink = styled(Link)`
    text-decoration: none;
`;

const SearchButton = styled.div`
    display: flex;
    padding: 18px 24px;
    justify-content: center;
    align-items: center;
    border-radius: 76px;
    background: #4a3aff;
    color: white;
    font-family: 'DM Sans', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 18px;
    margin: 1.5rem 0;

    &:hover {
        background: #6a40cc;
    }

    @media (max-width: 768px) {
        padding: 12px 16px;
        font-size: 1rem;
    }
`;

const HomepageSection = styled.div`
    margin-top: 3rem;
    width: 80%;
    max-width: 1200px;
    text-align: center;

    h2 {
        font-family: Inter, sans-serif;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    p {
        font-family: Inter, sans-serif;
        font-size: 16px;
        font-weight: 400;
        color: #666;
        margin-bottom: 2rem;
    }

    img {
        width: 80%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    @media (max-width: 768px) {
        h2 {
            font-size: 20px;
        }

        p {
            font-size: 14px;
        }

        img {
            width: 100%;
        }
    }
`;
