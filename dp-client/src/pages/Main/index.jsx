import React from 'react';
import { styled } from 'styled-components';
import { Link } from 'react-router-dom';
import advertiserBackground from '../../assets/advertiser.png';
import influencerBackground from '../../assets/influencer.png';
import LogoImg from '../../assets/Collabo.png';
import adverIcon from '../../assets/adicon.png';
import instaIcon from '../../assets/instaicon.png';
import arrow from '../../assets/ArrowRight.svg';

export default function Main() {
    return (
        <Wrapper>
            <Container>
                <Logo>
                    <img src={LogoImg} alt="Logo" />
                </Logo>
                <LeftSection>
                    <p>사업자이신가요?</p>
                    <Link to="/advertiser" style={{ textDecoration: 'none' }}>
                        <button>
                            <ButtonText>서비스 알아보기</ButtonText>
                            <ButtonIcon src={adverIcon} alt="광고주아이콘" />
                            <ColumnLine></ColumnLine>
                            <Arrow>
                                <img src={arrow} alt="화살표" />
                            </Arrow>
                        </button>
                    </Link>
                </LeftSection>
                <RightSection>
                    <p>인플루언서이신가요?</p>
                    <Link to="/influencer" style={{ textDecoration: 'none' }}>
                        <button>
                            <ButtonText>서비스 알아보기</ButtonText>
                            <ButtonIcon src={instaIcon} alt="인스타" />
                            <ColumnLine></ColumnLine>
                            <Arrow>
                                <img src={arrow} alt="화살표" />
                            </Arrow>
                        </button>
                    </Link>
                </RightSection>
            </Container>
        </Wrapper>
    );
}

const Wrapper = styled.div`
    position: relative;
    overflow: hidden;
    width: 100%;
    height: 100%;
    min-width: 1800px;

    margin: 0 auto;
    hr {
        height: 2px;
        background-color: gray;
    }
`;

const Logo = styled.div`
    display: flex;
    position: absolute;
    margin: 15px;
`;

const ColumnLine = styled.div`
    display: flex;
    position: absolute;
    width: 0px;
    right: 90px;
    height: 100%;
    border: 1px solid var(--black-10, rgba(28, 28, 28, 0.1));
`;
const Container = styled.div`
    display: flex;
    width: auto;
    height: auto;
    button {
        border: none;
        display: flex;
        position: relative;
        top: 300px;
        width: 22.25rem;
        height: 6rem;
        justify-content: center;
        align-items: center;
        border-radius: var(--16, 1rem);
        background: var(--Primary-Light, #f7f9fb);
        cursor: pointer;
        color: var(--black-100, #1c1c1c);
        font-family: Inter;
        font-size: 1.5rem;
        font-style: normal;
        font-weight: 600;
        line-height: 2.25rem;
        box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.2);
        &:hover {
            background: #ededed;
        }
    }
`;

const ButtonText = styled.span`
    position: relative;
    left: -17px;
`;

const ButtonIcon = styled.img`
    position: relative;
    left: -10px;
`;

const Arrow = styled.div`
    display: flex;
    position: relative;
    left: 20px;
`;
const LeftSection = styled.div`
    box-sizing: border-box;
    background-image: url(${advertiserBackground});
    background-size: cover;
    flex: 1;
    width: 1250px;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-right: -0.6rem;
    p {
        color: var(--white-100, #fff);
        text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        -webkit-text-stroke-width: 1;
        -webkit-text-stroke-color: var(--white-100, #fff);
        font-family: Inter;
        font-size: 64px;
        font-style: normal;
        font-weight: 700;
        line-height: 36px; /* 56.25% */
    }
`;

const RightSection = styled.div`
    background-image: url(${influencerBackground});
    background-size: cover;
    background-repeat: no-repeat;
    flex: 1;
    width: 1250px;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: none;

    p {
        color: var(--white-100, #fff);
        text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        -webkit-text-stroke-width: 1;
        -webkit-text-stroke-color: var(--white-100, #fff);
        font-family: Inter;
        font-size: 64px;
        font-style: normal;
        font-weight: 700;
        line-height: 36px;
    }
`;
