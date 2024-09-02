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
        <Wrapper>
            <Nav>
                <Logo to="/influencer">
                    <img src={LogoImg} alt="Logo" />
                </Logo>
                <Links>
                    <NavLink to="/report">내 리포트</NavLink>
                    <NavLink to="/*">인플루언서 찾기</NavLink>
                    <NavLink to="/*">캠페인 등록</NavLink>
                    <NavLink to="/influmypage">마이페이지</NavLink>
                </Links>
                <RightMenu>
                    {isLoggedIn ? (
                        <LoginButton onClick={handleLogout}>Login</LoginButton>
                    ) : (
                        <LoginButton onClick={handleLogin}>Logout</LoginButton>
                    )}
                    <GetStartButton>Get Started</GetStartButton>
                </RightMenu>
            </Nav>
        </Wrapper>
    );
};

const Wrapper = styled.nav`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    min-width: 1500px;
    white-space: nowrap;
    border-bottom: 0.7px solid #dbe0de;
    position: relative;
    background-color: #ffffff;
`;

const Nav = styled.nav`
    width: 100%;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100px;
    background-color: #fff;
    overflow: hidden;
`;

const Logo = styled(Link)`
    text-decoration: none;
    margin-left: 200px;
`;

const Links = styled.div`
    display: flex;
    list-style: none;
    gap: 40px;
    cursor: pointer;
`;
const RightMenu = styled.div`
    display: flex;
    align-items: center;
    gap: 15px;
    margin-right: 200px;
`;
const NavLink = styled(Link)`
    color: var(--Neutral-800, #170f49);
    text-align: center;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: 20px; /* 111.111% */
    transition: transform 0.2s ease-in-out;
    margin-top: 10px;

    &:hover {
        color: #a338f6;
        transform: scale(1.1);
        cursor: pointer;
    }
`;
const LoginButton = styled(Link)`
    display: flex;
    padding: 18px 24px;
    justify-content: center;
    align-items: center;
    gap: 4px;
    border-radius: 75.999px;
    border: 1px solid var(--Neutral-400, #d9dbe9);
    background: var(--white-100, #fff);
    color: var(--Neutral-800, #170f49);
    text-align: center;
    font-feature-settings: 'liga' off, 'clig' off;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: 18px; /* 112.5% */
`;

const GetStartButton = styled(Link)`
    display: flex;
    padding: 18px 24px;
    justify-content: center;
    align-items: center;
    gap: 4px;
    border-radius: 75.999px;
    background: var(--Primary-Color-1, #4a3aff);
    color: var(--Neutral-100, var(--white-100, #fff));
    text-align: center;
    font-feature-settings: 'liga' off, 'clig' off;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 18px; /* 112.5% */
`;
export default InfluencerNavbar;
