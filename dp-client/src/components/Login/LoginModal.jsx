import React from 'react';
import styled from 'styled-components';
import LogoImg from '../../assets/Collabo.png';
const LoginModal = ({ show, onClose }) => {
    if (!show) {
        return null;
    }

    return (
        <Overlay>
            <Modal>
                <CloseButton onClick={onClose}>&times;</CloseButton>
                <Wrapper>
                    <Logo>
                        <img src={LogoImg} alt="Logo" />
                    </Logo>
                    <p>Log in</p>
                    <p2>계정이 없으신가요? 회원가입하세요.</p2>
                    <AdSignupButton>사업자 회원가입</AdSignupButton>
                    <InfluSignupButton>인플루언서 회원가입</InfluSignupButton>
                    <hr></hr>
                    <Form>
                        <Label>Your email</Label>
                        <Input type="email" placeholder="이메일을 입력해주세요." />
                        <Label>Your password</Label>
                        <Input type="password" placeholder="비밀번호를 입력해주세요." />
                        <ForgotPasswordLink>Forget your password</ForgotPasswordLink>
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

const AdSignupButton = styled.div`
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
