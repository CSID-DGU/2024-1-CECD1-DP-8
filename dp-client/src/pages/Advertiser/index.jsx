import React from 'react';
import AdvertiserNavbar from '../../components/Navbar/AdvertiserNavbar';
import { styled } from 'styled-components';
import { Link } from 'react-router-dom';

export default function AdvertiserMain() {
    return (
        <>
            <AdvertiserNavbar></AdvertiserNavbar>

            <Wrapper>
                <IntroWrapper>
                    <a>인플루언서 추천</a>
                    <h1>
                        원하는 인플루언서를 쉽고 <br />
                        편하게 찾아보세요!
                    </h1>
                </IntroWrapper>
                <StyledLink to="/matchingpage">
                    <SearchButton>인플루언서 추천 받기</SearchButton>
                </StyledLink>
                <HomepageSection>
                    <h2>필터링과 키워드로 탐색하세요.</h2>
                    <p>
                        카테고리 (관심 분야), 팔로워수, 성별, 해시태그 등을 선택하세요. 해당 필터 조건에 맞춰 원하는
                        인플루언서 리스트를 바로 확인할 수 있습니다.
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
`;

const IntroWrapper = styled.div`
    display: flex;
    margin-top: 5rem;
    width: 660px;
    height: 271px;
    flex-shrink: 0;
    flex-direction: column;
    text-align: center;
    a {
        color: #780bc2;
        text-align: center;
        font-family: Inter;
        font-size: 25px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
        background: linear-gradient(180deg, #780bc2 0%, #39055c 100%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    h1 {
        background: linear-gradient(180deg, #4017e3 0%, #230d7d 83%);
        background-clip: text;
        margin-top: 2rem;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: Inter;
        font-size: 48px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }
`;

const StyledLink = styled(Link)`
    text-decoration: none;
`;

const SearchButton = styled.div`
    text-decoration: none;
    display: flex;
    padding: 18px 24px;
    justify-content: center;
    align-items: center;
    gap: 4px;
    align-items: center;
    border-radius: 76px;
    background: var(--Primary-Color-1, #4a3aff);
    color: var(--Neutral-100, var(--white-100, #fff));
    text-align: center;
    font-family: 'DM Sans';
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 700;
    line-height: 18px; /* 112.5% */
`;

const HomepageSection = styled.div`
    margin-top: 3rem;
    text-align: left;
    width: 80%;
    max-width: 1200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    h2 {
        font-family: Inter;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    p {
        font-family: Inter;
        font-size: 16px;
        font-weight: 400;
        color: #666;
        margin-bottom: 2rem;
    }
    img {
        width: 50%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
`;
