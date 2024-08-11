import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import LogoImg from '../../assets/Collabo.png';

const InfluencerNavbar = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    // 로그인 버튼 클릭 시 로그인 상태 변경
    const handleLogin = () => {
        setIsLoggedIn(true);
    };

    // 로그아웃 버튼 클릭 시 로그인 상태 변경
    const handleLogout = () => {
        setIsLoggedIn(false);
    };

    return (
        <Nav>
            <Logo to="/influencer">
                <img src={LogoImg} alt="Logo" />
            </Logo>
            <Links>
                <NavLink to="/report">내 리포트</NavLink>
                <NavLink to="/influmypage">마이페이지</NavLink>
                {isLoggedIn ? (
                    <LoginButton onClick={handleLogout}>로그아웃</LoginButton>
                ) : (
                    <LoginButton onClick={handleLogin}>로그인</LoginButton>
                )}
                <GetStartButton>Get Started</GetStartButton>
            </Links>
        </Nav>
    );
};

const Nav = styled.nav`
    background-color: #ffffff;
    display: flex;
    width: 100%;
    height: 120px;
    align-items: center;
`;

const Logo = styled(Link)`
    font-size: 1.5rem;
    text-decoration: none;
    margin-left: 4rem;
`;

const Links = styled.div`
    display: flex;
    gap: 4rem;
    margin-left: 600px;
`;

const NavLink = styled(Link)`
    color: #170f49;
    text-decoration: none;
    color: var(--Neutral-800, #170f49);
    text-align: center;
    font-family: 'DM Sans';
    font-size: 30px;
    font-style: normal;
    font-weight: 400;
    line-height: 20px; /* 111.111% */
    transition: transform 0.2s ease-in-out;
    margin-top: 30px;

    &:hover {
        color: #a338f6;
        transform: scale(1.1);
        cursor: pointer;
    }
`;
const LoginButton = styled(Link)`
    font-family: 'DM Sans';
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 700;
    line-height: 18px;
    text-decoration: none;
    margin-left: 6rem;
    display: flex;
    padding: 18px 24px;
    width: 100px;
    justify-content: center;
    align-items: center;
    margin-top: 0.5rem;
    border-radius: 76px;
    border: 1px solid var(--Neutral-400, #d9dbe9);
    background: var(--Neutral-100, #fff);
`;

const GetStartButton = styled(Link)`
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
    margin-top: 0.5rem;
    font-family: 'DM Sans';
    font-size: 1.5rem;
    font-style: normal;
    font-weight: 700;
    line-height: 18px; /* 112.5% */
`;
export default InfluencerNavbar;
