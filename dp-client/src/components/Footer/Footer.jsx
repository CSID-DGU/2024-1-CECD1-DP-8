import styled from 'styled-components';
import { Link, useNavigate } from 'react-router-dom';
import logo from '../../assets/Collabo.png';

export default function Footer() {
    const navigate = useNavigate();
    return (
        <FooterWrapper>
            <FooterContainer>
                <LeftSection>
                    <Logo src={logo} alt="LocalMark Logo" onClick={() => navigate('/')} />
                    <LinkRow>
                        <StyledLink to="/privacy">개인정보처리방침</StyledLink>
                        <StyledLink to="/terms">이용약관</StyledLink>
                    </LinkRow>
                    <Copyright>ⓒ 2024. COLLABO All rights reserved.</Copyright>
                </LeftSection>
                <RightSection>
                    <Column>
                        <StyledLink to="/">랜딩 페이지</StyledLink>
                    </Column>
                    <Column>
                        <StyledLink to="/matchingPage2">인플루언서 추천</StyledLink>
                        {/* <SubMenu>
                            <StyledLink to="/"></StyledLink>
                            <StyledLink to="/">이벤트</StyledLink>
                        </SubMenu> */}
                    </Column>
                    <Column>
                        <StyledLink to="/">인플루언서 찾기</StyledLink>
                    </Column>
                    <Column>
                        <StyledLink to="/">캠페인 등록</StyledLink>
                    </Column>
                    <Column>
                        <StyledLink to="/admypage">마이페이지</StyledLink>
                    </Column>
                </RightSection>
            </FooterContainer>
        </FooterWrapper>
    );
}

const FooterWrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    min-width: 1300px;
    height: 296px;
    padding: 50px 354px 118.109px 360px;
    border-top: 0.5px solid var(--Color-Gray-gray-400, #bdbdbd);
    background: var(--Color-Background-light-gray, #fafafa);
    box-sizing: border-box;
`;

const FooterContainer = styled.div`
    display: flex;
    justify-content: space-between;
    width: 100%;
    white-space: nowrap;
`;

const LeftSection = styled.div`
    display: flex;
    flex-direction: column;
    gap: 20px;
`;

const LinkRow = styled.div`
    display: flex;
    gap: 20px;
    margin-top: -20px;
    color: var(--Color-Text-primary, #222);
    font-size: 14px;
    font-style: normal;
    font-weight: 400;
    line-height: 140%;
    letter-spacing: -0.28px;
`;

const RightSection = styled.div`
    display: flex;
    justify-content: space-between;
    width: 40%;
    max-width: 800px;
    gap: 60px;
    margin-top: 35px;
    color: var(--Color-Text-primary, #222);
    font-size: var(--Text-size-4, 16px);
    font-style: normal;
    font-weight: 600;
    line-height: 140%;
    letter-spacing: -0.32px;
`;

const Column = styled.div`
    display: flex;
    flex-direction: column;
    gap: 10px;
`;

const Logo = styled.img`
    width: 190px;
    height: auto;
    cursor: pointer;
    margin-bottom: 10px;
`;

const Copyright = styled.div`
    color: #666;
    font-size: 14px;
`;

const SubMenu = styled.div`
    display: flex;
    flex-direction: column;
    margin-top: 5px;
    gap: 15px;
    font-size: var(--Text-size-3, 14px);
    font-style: normal;
    font-weight: 400;
    line-height: 140%;
    letter-spacing: -0.28px;
    text-align: center;
`;

const StyledLink = styled(Link)`
    text-decoration: none;
    color: inherit;
    white-space: nowrap;
`;
