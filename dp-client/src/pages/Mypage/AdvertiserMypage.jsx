import React from 'react';
import AdvertiserNavbar from '../../components/Navbar/AdvertiserNavbar';
import { styled } from 'styled-components';

export default function AdvertiserMypage() {
    return (
        <>
            <AdvertiserNavbar></AdvertiserNavbar>
            <Wrapper>
                <div>사업자 마이페이지입니다.</div>
            </Wrapper>
        </>
    );
}

const Wrapper = styled.div`
    width: 100%;
    height: 100%;
    display: flex;
`;
