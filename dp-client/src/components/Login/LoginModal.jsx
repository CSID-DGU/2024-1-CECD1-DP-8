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
                        <ButtonContainer>
                            <LoginButton>Log in</LoginButton>
                        </ButtonContainer>
                    </Form>
                </Wrapper>
            </Modal>
        </Overlay>
    );
};
const FacebookButton = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    width: 100%;
    max-width: 528px;
    height: 60px;
    background: #1877f2;
    border-radius: 12px;
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    &:hover {
        background: #145dbf;
        transform: translateY(-2px);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }
`;

const KakaoButton = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    width: 100%;
    max-width: 528px;
    height: 60px;
    background: #fee500;
    border-radius: 12px;
    color: #3c1e1e;
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);

    &:hover {
        background: #f2d700;
        transform: translateY(-2px);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }
`;

const Input = styled.input`
    height: 56px;
    align-self: stretch;
    border-radius: 12px;
    border: 1px solid rgba(102, 102, 102, 0.35);
    width: 100%;
    padding: 0.5rem 1rem;
    font-size: 16px;
    font-family: 'Poppins', sans-serif;
    transition: all 0.3s ease-in-out;

    &:focus {
        outline: none;
        border-color: #463392;
        box-shadow: 0px 0px 8px rgba(70, 51, 146, 0.4);
    }
`;
const ButtonContainer = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
`;
const LoginButton = styled.button`
    display: flex;
    justify-content: center;
    align-items: center;
    width: 350px;
    max-width: 528px;
    height: 55px;
    background: #463392;
    color: white;
    font-size: 18px;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);

    &:hover {
        background: #352366;
        transform: translateY(-2px);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }
`;

const ForgotPasswordLink = styled.a`
    font-size: 14px;
    color: #463392;
    cursor: pointer;
    text-decoration: none;
    font-family: 'Poppins', sans-serif;

    &:hover {
        text-decoration: underline;
        color: #352366;
    }
`;

const Separator = styled.hr`
    width: 100%;
    max-width: 528px;
    border: none;
    height: 1px;
    background-color: rgba(102, 102, 102, 0.25);
    margin: 2rem 0;
`;

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
    width: 705px;
    height: 700px;
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
    padding-top: 50px;
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

const LogoIcon = styled.img`
    width: 24px;
    height: 24px;
    margin-right: 12px;
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

const SubContainer = styled.div`
    display: flex;
    flex-direction: row;
    gap: 20px;
    justify-content: flex-end;
`;

export default LoginModal;
