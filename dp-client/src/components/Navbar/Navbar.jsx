import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import LogoImg from '../../assets/Collabo.svg';
import LoginModal from '../Login/LoginModal';

const Navbar = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showLoginModal, setShowLoginModal] = useState(false);

    // 로그인 버튼 클릭 시 로그인 상태 변경
    const handleLogin = () => {
        setShowLoginModal(true); // 로그인 모달 열기
    };

    // 로그아웃 버튼 클릭 시 로그인 상태 변경
    const handleLogout = () => {
        setIsLoggedIn(false);
    };

    // 로그인 모달 닫기
    const closeLoginModal = () => {
        setShowLoginModal(false);
    };

    return (
        <>
            <Wrapper>
                <Nav>
                    <Logo to="/">
                        <img src={LogoImg} alt="Logo" />
                    </Logo>
                    <Links>
                        <NavLink to="/recommend">인플루언서 추천</NavLink>
                        <NavLink to="/report">인플루언서 리포트</NavLink>
                    </Links>
                    <RightMenu>
                        {isLoggedIn ? (
                            <LoginButton as="button" onClick={handleLogout}>
                                Logout
                            </LoginButton>
                        ) : (
                            <LoginButton as="button" onClick={handleLogin}>
                                Login
                            </LoginButton>
                        )}
                    </RightMenu>
                </Nav>
            </Wrapper>
            {/* 로그인 모달 */}
            {showLoginModal && <LoginModal show={showLoginModal} onClose={closeLoginModal} />}
        </>
    );
};

const Wrapper = styled.nav`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    min-width: 1200px;
    white-space: nowrap;
    border-bottom: 0.7px solid #dbe0de;
    position: relative;
    background-color: #ffffff;

    @media (max-width: 768px) {
        min-width: 100%; /* 모바일에서 전체 너비로 조정 */
        height: auto;
    }
`;

const Nav = styled.nav`
    width: 100%;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100px;
    background-color: #fff;

    @media (max-width: 768px) {
        flex-direction: row; /* 모바일에서도 수평 정렬 */
        height: auto;
        padding: 10px 15px;
    }
`;

const Logo = styled(Link)`
    text-decoration: none;
    margin-left: 50px;

    img {
        height: 40px;
        transition: height 0.3s ease;

        @media (max-width: 768px) {
            height: 30px; /* 모바일에서 로고 크기 조정 */
        }
    }

    @media (max-width: 768px) {
        margin-left: 10px; /* 모바일에서 왼쪽 상단에 위치 */
    }
`;

const Links = styled.div`
    display: flex;
    list-style: none;
    gap: 150px;
    cursor: pointer;

    @media (max-width: 768px) {
        gap: 10px; /* 모바일에서 링크 간격 조정 */
        flex-wrap: wrap; /* 링크를 줄바꿈 가능하도록 */
        justify-content: center;
        margin: 10px 0; /* 모바일에서 상하 여백 추가 */
    }
`;

const RightMenu = styled.div`
    display: flex;
    align-items: center;
    gap: 15px;
    margin-right: 200px;

    @media (max-width: 768px) {
        margin-right: 10px; /* 모바일에서 오른쪽 상단에 위치 */
        margin-top: 0;
    }
`;

const NavLink = styled(Link)`
    color: var(--Neutral-800, #170f49);
    text-align: center;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: 20px; /* 111.111% */
    transition: transform 0.2s ease-in-out;

    &:hover {
        color: #a338f6;
        transform: scale(1.1);
        cursor: pointer;
    }

    @media (max-width: 768px) {
        font-size: 14px; /* 모바일에서 링크 글꼴 크기 축소 */
    }
`;

const LoginButton = styled.button`
    display: flex;
    padding: 18px 24px;
    justify-content: center;
    align-items: center;
    gap: 4px;
    border-radius: 75.999px;
    border: 1px solid var(--Neutral-400, #d9dbe9);
    background: var(--Primary-Color-1, #4a3aff);
    color: var(--Neutral-100, var(--white-100, #fff));
    text-align: center;
    font-feature-settings: 'liga' off, 'clig' off;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: 18px; /* 112.5% */
    cursor: pointer;

    &:hover {
        background: #9997f7;
    }

    @media (max-width: 768px) {
        font-size: 14px;
        padding: 10px 20px;
    }
`;

export default Navbar;
