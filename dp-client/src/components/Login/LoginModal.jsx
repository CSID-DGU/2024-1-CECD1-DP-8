import React, { useEffect } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import LogoImg from '../../assets/Collabo.png';
import FacebookLogo from '../../assets/facebook-logo.png'; // 페이스북 로고 추가
import KakaoLogo from '../../assets/kakao-logo.png'; // 카카오 로고 추가

const LoginModal = ({ show, onClose }) => {
    const navigate = useNavigate();

    // 환경 변수에서 APP ID를 불러옵니다.
    const facebookAppId = process.env.REACT_APP_FACEBOOK_APP_ID;
    const kakaoRestApiKey = process.env.REACT_APP_KAKAO_REST_API_KEY;

    // NODE_ENV로 환경에 따른 Redirect URI 설정
    const kakaoRedirectUri =
        process.env.NODE_ENV === 'production' ? 'https://cecd-dp.netlify.app/oauth' : 'http://localhost:3000/oauth';
    useEffect(() => {
        // 페이스북 SDK 초기화
        window.fbAsyncInit = function () {
            window.FB.init({
                appId: facebookAppId,
                autoLogAppEvents: true,
                xfbml: true,
                version: 'v12.0',
            });
        };

        // 페이스북 SDK 로드
        (function (d, s, id) {
            var js,
                fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id)) return;
            js = d.createElement(s);
            js.id = id;
            js.src = 'https://connect.facebook.net/en_US/sdk.js';
            fjs.parentNode.insertBefore(js, fjs);
        })(document, 'script', 'facebook-jssdk');
    }, [facebookAppId]);

    // 페이스북 로그인 핸들러
    const handleFacebookLogin = () => {
        window.FB.login(
            function (response) {
                if (response.authResponse) {
                    const accessToken = response.authResponse.accessToken;
                    console.log('페이스북 로그인 성공!', accessToken);
                    // 서버에 accessToken 전달 후 로그인 처리
                    navigate('/'); // 예시: 로그인 후 리디렉션
                } else {
                    console.log('페이스북 로그인 실패');
                }
            },
            { scope: 'public_profile,email' }
        );
    };

    // 카카오 로그인 핸들러
    const handleKakaoLogin = () => {
        const kakaoURL = `https://kauth.kakao.com/oauth/authorize?client_id=${kakaoRestApiKey}&redirect_uri=${kakaoRedirectUri}&response_type=code`;
        window.location.href = kakaoURL;
    };

    if (!show) {
        return null;
    }

    const handleSignup = () => {
        navigate('/signup'); // 회원가입 버튼 클릭 시 /signup 경로로 이동
    };

    return (
        <Overlay>
            <Modal>
                <CloseButton onClick={onClose}>&times;</CloseButton>
                <Wrapper>
                    <Logo>
                        <img src={LogoImg} alt="Logo" />
                    </Logo>
                    <SubText>로그인</SubText>
                    <FacebookButton onClick={handleFacebookLogin}>
                        <LogoIcon src={FacebookLogo} alt="Facebook logo" />
                        페이스북으로 로그인
                    </FacebookButton>
                    <KakaoButton onClick={handleKakaoLogin}>
                        <LogoIcon src={KakaoLogo} alt="Kakao logo" />
                        카카오로 로그인
                    </KakaoButton>
                    <Separator />
                    <Form>
                        <Label>Your email</Label>
                        <Input type="email" placeholder="이메일을 입력해주세요." />
                        <Label>Your password</Label>
                        <Input type="password" placeholder="비밀번호를 입력해주세요." />
                        <SubContainer>
                            <ForgotPasswordLink onClick={handleSignup}>회원가입</ForgotPasswordLink>
                            <ForgotPasswordLink>비밀번호 찾기</ForgotPasswordLink>
                        </SubContainer>
                        <LoginButton>Log in</LoginButton>
                    </Form>
                </Wrapper>
            </Modal>
        </Overlay>
    );
};

const Overlay = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
`;

const Modal = styled.div`
    background: white;
    padding: 20px;
    border-radius: 24px;
    width: 795px;
    height: 861px;
    max-width: 90%;
    position: relative;
`;

const Logo = styled.div`
    font-size: 1.5rem;
    text-decoration: none;
    margin: 3rem;
`;

const CloseButton = styled.button`
    background: none;
    border: none;
    font-size: 1.5rem;
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
`;

const Wrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
    p {
        color: #333;
        text-align: center;
        font-family: Poppins;
        font-size: 32px;
        font-style: normal;
        font-weight: 500;
        line-height: normal;
        margin-bottom: 1rem;
    }
`;

const SubText = styled.p`
    font-family: Poppins, sans-serif;
    font-size: 18px;
    color: #666;
    margin-bottom: 1.5rem;
`;

const FacebookButton = styled.div`
    display: flex;
    width: 528px;
    height: 60px;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    background: #3b5998;
    color: #fff;
    font-family: Arial, sans-serif;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    margin-bottom: 1rem;
    &:hover {
        background: #2d4373;
    }
`;

const KakaoButton = styled.div`
    display: flex;
    width: 528px;
    height: 60px;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    background: #fee500;
    color: #3c1e1e;
    font-family: Arial, sans-serif;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    margin-bottom: 2rem;
    &:hover {
        background: #f2d700;
    }
`;

const LogoIcon = styled.img`
    width: 24px;
    height: 24px;
    margin-right: 12px;
`;

const Separator = styled.hr`
    width: 528px;
    border: none;
    height: 2px;
    background-color: rgba(102, 102, 102, 0.25);
    margin-top: 2rem;
    margin-bottom: 2rem;
`;

const Form = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 528px;
    margin-top: 1rem;
`;

const Label = styled.label`
    margin-bottom: 0.5rem;
    color: #333;
    font-family: Inter;
    font-size: 16px;
`;

const Input = styled.input`
    height: 56px;
    align-self: stretch;
    border-radius: 8px;
    border: 1px solid rgba(102, 102, 102, 0.35);
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
`;

const ForgotPasswordLink = styled.a`
    align-self: flex-end;
    margin-bottom: 1rem;
    cursor: pointer;
    color: #333;
    text-decoration: none;
    &:hover {
        text-decoration: underline;
    }
`;

const SubContainer = styled.div`
    display: flex;
    flex-direction: row;
    gap: 20px;
    justify-content: flex-end;
`;

const LoginButton = styled.button`
    display: flex;
    width: 528px;
    height: 64px;
    padding: 15px 0px 16px 0px;
    justify-content: center;
    align-items: center;
    background-color: #ccc;
    border: none;
    border-radius: 20px;
    color: white;
    font-size: 22px;
    font-style: normal;
    font-weight: 500;
    cursor: pointer;
    &:hover {
        background-color: #bbb;
    }
`;

export default LoginModal;
