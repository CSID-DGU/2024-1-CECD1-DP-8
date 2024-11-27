// src/components/Spinner/Spinner.jsx
import React from 'react';
import styled, { keyframes } from 'styled-components';

const Spinner = () => {
    return (
        <SpinnerOverlay>
            <SpinnerContainer />
        </SpinnerOverlay>
    );
};

export default Spinner;

const spin = keyframes`
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
`;

const SpinnerOverlay = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
`;

const SpinnerContainer = styled.div`
    border: 8px solid rgba(0, 0, 0, 0.1);
    border-top: 8px solid #4a3aff;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: ${spin} 1s linear infinite;
`;
