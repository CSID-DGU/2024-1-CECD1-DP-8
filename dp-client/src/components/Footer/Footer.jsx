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
                        <StyledLink to="/recommend">인플루언서 추천</StyledLink>
                    </Column>

                    <Column>
                        <StyledLink to="/report">인플루언서 리포트</StyledLink>
                    </Column>
                    <Column>
                        <StyledLink
                            to="/influmypage
                        "
                        >
                            마이페이지
                        </StyledLink>
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
    justify-content: center;
    width: 100%;
    height: auto;
    padding: 40px 20px; /* 위아래 패딩 조정 */
    border-top: 1px solid #bdbdbd;
    background: #fafafa;
    box-sizing: border-box;
`;

const FooterContainer = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1200px; /* 최대 너비 설정 */
    flex-wrap: wrap; /* 화면 크기에 따라 자동 줄바꿈 */
    gap: 20px;
`;

const LeftSection = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start; /* 왼쪽 정렬 */
    gap: 15px;
`;

const RightSection = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap; /* 작은 화면에서 자동 줄바꿈 */
    width: 100%;
    max-width: 600px;
    gap: 20px;
`;

const Column = styled.div`
    display: flex;
    flex-direction: column;
    gap: 10px;
`;

const Logo = styled.img`
    width: 120px; /* 로고 크기 조정 */
    height: auto;
    cursor: pointer;
`;

const LinkRow = styled.div`
    display: flex;
    flex-wrap: wrap; /* 작은 화면에서 링크를 줄바꿈 */
    gap: 15px;
    font-size: 14px;
    color: #222;
    line-height: 1.4;
`;

const Copyright = styled.div`
    font-size: 12px;
    color: #666;
    text-align: left;
`;

const StyledLink = styled(Link)`
    text-decoration: none;
    color: inherit;
    font-size: 14px;
    white-space: nowrap;
`;
