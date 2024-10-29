import React, { useEffect } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import LogoImg from '../../assets/Collabo.png';

const LoginModal = ({ show, onClose }) => {
    const navigate = useNavigate();

    useEffect(() => {
        // 페이스북 SDK 초기화
        window.fbAsyncInit = function () {
            window.FB.init({
                appId: '541978015128322', // 제공한 페이스북 앱 ID 사용
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
    }, []);

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
                    <p>Log in</p>
                    <p2>소셜 로그인으로 간단하게 로그인 하세요.</p2>
                    <SocialLoginButton onClick={handleFacebookLogin}>페이스북 로그인</SocialLoginButton>
                    <hr></hr>
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
    p2 {
        display: flex;
        padding: 2px;
        align-items: flex-start;
        gap: 10px;
        margin-bottom: 0.8rem;
    }
    hr {
        margin-top: 3rem;
        height: 2px;
        background: rgba(102, 102, 102, 0.25);
        width: 528px;
    }
`;

const SocialLoginButton = styled.div`
    display: flex;
    width: 528px;
    height: 72px;
    margin-bottom: 20px;
    justify-content: center;
    align-items: center;
    border-radius: 40px;
    border: 2px solid #333;
    background: #fff;
    color: #333;
    font-family: Inter;
    font-size: 22px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    cursor: pointer;
    &:hover {
        background: #f0f0f0;
    }
`;

const InfluSignupButton = styled.div`
    display: flex;
    width: 528px;
    height: 72px;
    justify-content: center;
    align-items: center;
    border-radius: 40px;
    border: 2px solid #333;
    background: #fff;
    color: #333;
    font-family: Inter;
    font-size: 22px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    cursor: pointer;
    &:hover {
        background: #f0f0f0;
    }
`;
const Form = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 528px;
    margin-top: 2rem;
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
    border-radius: var(--12, 12px);
    border: 1px solid rgba(102, 102, 102, 0.35);
    width: 100%;
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
