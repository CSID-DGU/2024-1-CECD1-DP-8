import React from 'react';
import CompanyNavbar from '../../components/Navbar/AdvertiserNavbar';
import { styled } from 'styled-components';

export default function AdvertiserMain() {
    return (
        <>
            <CompanyNavbar></CompanyNavbar>

            <Wrapper>
                <div>사업자 메인</div>
            </Wrapper>
        </>
    );
}

const Wrapper = styled.div`
    width: 100%;
    height: 100%;
    display: flex;
`;
