// src/pages/NotFound/NotFound.jsx
import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const NotFound = () => {
    return (
        <NotFoundContainer>
            <Title>404</Title>
            <Subtitle>페이지를 찾을 수 없습니다</Subtitle>
            <HomeButton to="/">홈으로 돌아가기</HomeButton>
        </NotFoundContainer>
    );
};

export default NotFound;

const NotFoundContainer = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(180deg, #f8f9fa 0%, #e0e7ff 100%);
`;

const Title = styled.h1`
    font-size: 8rem;
    font-weight: 800;
    color: #4a3aff;
`;

const Subtitle = styled.p`
    font-size: 1.5rem;
    color: #6c757d;
    margin: 1rem 0;
`;

const HomeButton = styled(Link)`
    padding: 10px 20px;
    border-radius: 30px;
    background-color: #4a3aff;
    color: #fff;
    text-decoration: none;
    font-size: 1rem;
    transition: background-color 0.3s;

    &:hover {
        background-color: #3629d1;
    }
`;
