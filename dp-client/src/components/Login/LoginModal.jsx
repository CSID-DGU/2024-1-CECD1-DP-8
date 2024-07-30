import React, { useState } from 'react';
import { styled } from 'styled-components';

export default function LoginModal() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [age, setAge] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [nameMessage, setNameMessage] = useState('');
    const [emailMessage, setEmailMessage] = useState('');
    const [ageMessage, setAgeMessage] = useState('');
    const [passwordMessage, setPasswordMessage] = useState('');
    const [confirmPasswordMessage, setConfirmPasswordMessage] = useState('');
    const [modalVisible, setModalVisible] = useState(false);

    const validateFields = () => {
        let isValid = true;

        // 이름 필드 유효성 검사
        if (name.trim() === '') {
            setNameMessage({ message: '필수 입력 항목입니다!', success: false });
            isValid = false;
        } else {
            setNameMessage({ message: '멋진 이름이네요!', success: true });
        }

        // 이메일 필드 유효성 검사
        if (!email.includes('@')) {
            setEmailMessage({ message: '올바른 이메일 형식이 아닙니다!', success: false });
            isValid = false;
        } else {
            setEmailMessage({ message: '올바른 이메일 형식입니다!', success: true });
        }

        // 나이 필드 유효성 검사
        const ageNumber = parseInt(age);
        if (isNaN(ageNumber)) {
            setAgeMessage({ message: '숫자를 입력해주세요!', success: false });
            isValid = false;
        } else if (ageNumber !== parseFloat(age)) {
            setAgeMessage({ message: '나이는 소수가 될 수 없습니다!', success: false });
            isValid = false;
        } else if (ageNumber < 0) {
            setAgeMessage({ message: '나이는 음수가 될 수 없습니다!', success: false });
            isValid = false;
        } else if (ageNumber < 19) {
            setAgeMessage({ message: '미성년자는 가입할 수 없습니다!', success: false });
            isValid = false;
        } else {
            setAgeMessage({ message: '올바른 나이 형식입니다!', success: true });
        }

        // 비밀번호 필드 유효성 검사
        if (password.length < 4) {
            setPasswordMessage({ message: '최소 4자리 이상이어야 합니다.', success: false });
            isValid = false;
        } else if (password.length > 12) {
            setPasswordMessage({ message: '최대 12자리까지 가능합니다.', success: false });
            isValid = false;
        } else if (!/[a-zA-Z]/.test(password) || !/\d/.test(password) || !/[^a-zA-Z\d]/.test(password)) {
            setPasswordMessage({
                message: '영문, 숫자, 특수문자를 모두 포함해야 합니다.',
                success: false,
            });
            isValid = false;
        } else {
            setPasswordMessage({ message: '올바른 비밀번호입니다!', success: true });
        }

        // 비밀번호 확인 필드 유효성 검사
        if (confirmPassword !== password) {
            setConfirmPasswordMessage({ message: '비밀번호가 일치하지 않습니다!', success: false });
            isValid = false;
        } else if (confirmPassword === '') {
            setConfirmPasswordMessage({ message: '비밀번호가 일치하지 않습니다!', success: false });
            isValid = false;
        } else {
            setConfirmPasswordMessage({ message: '비밀번호가 일치합니다!', success: true });
        }

        return isValid;
    };

    const handleSignUp = () => {
        const isValid = validateFields();
        if (isValid) {
            // 가입 처리
            setModalVisible(true); // 모달 띄우기
        }
    };

    return (
        <>
            {/* 모달 컴포넌트 추가 */}
            {modalVisible && (
                <Modal>
                    <h2>가입 성공!</h2>
                    <br />
                    <button onClick={() => setModalVisible(false)}>확인</button>
                </Modal>
            )}
            <Container>
                <SignUpContainer>
                    <h1>회원가입</h1>
                    <HeadLine></HeadLine>
                    <InputForm>
                        <p>이름</p>
                        <InputField type="text" placeholder="" value={name} onChange={(e) => setName(e.target.value)} />
                        <Message success={nameMessage.success}>{nameMessage.message}</Message>
                        <p>이메일</p>
                        <InputField
                            type="text"
                            placeholder=""
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <Message success={emailMessage.success}>{emailMessage.message}</Message>
                        <p>나이</p>
                        <InputField type="text" placeholder="" value={age} onChange={(e) => setAge(e.target.value)} />
                        <Message success={ageMessage.success}>{ageMessage.message}</Message>
                        <p>비밀번호</p>
                        <InputField
                            type="password"
                            placeholder=""
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <Message success={passwordMessage.success}>{passwordMessage.message}</Message>
                        <p>비밀번호 확인</p>
                        <InputField
                            type="password"
                            placeholder=""
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                        />
                        <Message success={confirmPasswordMessage.success}>{confirmPasswordMessage.message}</Message>
                    </InputForm>
                    <SignupButton onClick={handleSignUp}>
                        <p>가입하기</p>
                    </SignupButton>
                </SignUpContainer>
            </Container>
        </>
    );
}

const Container = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    position: relative;
    height: 100vw;
    display: flex;
    background-color: #bde7fa;
    margin: 0 auto;
`;

const SignUpContainer = styled.div`
    display: flex;
    flex-direction: column;
    width: 900px;
    height: 1000px;
    background-color: #d7effa;
    border-radius: 1rem;
    margin-top: 5rem;
    align-items: center;
    box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.2);

    h1 {
        text-align: center;
        margin-top: 60px;
        font-style: bold;
    }
`;

const HeadLine = styled.div`
    width: 600px;
    position: relative;
    height: 2px;
    display: flex;
    background-color: white;
    margin: 0 auto;
    margin-bottom: -10rem;
`;

const InputForm = styled.div`
    display: flex;
    flex-direction: column;
    width: 700px;
    height: auto;
    margin: auto 0;
    p {
        color: black;
        font-size: 1.2rem;
        font-weight: 800;
        line-height: 100%;
    }
`;

const InputField = styled.input`
    width: 99%;
    height: 3rem;
    border-radius: 1rem;
    border: 3px solid white;
    background-color: #d7effa;
`;

const Message = styled.div`
    color: ${({ success }) => (success ? 'green' : 'red')};
    font-size: 1.2rem;
    font-weight: 800;
    line-height: 100%;
`;

const SignupButton = styled.button`
    margin-bottom: 2rem;
    margin-top: -10rem;
    width: 20rem;
    height: 4rem;
    flex-shrink: 0;
    border-radius: 0.9375rem;
    background: #959595;
    border: none;
    cursor: pointer;
    p {
        color: white;
        text-align: center;
        font-size: 1.1rem;
        font-style: bold;
        font-weight: 800;
        line-height: 100%;
    }
`;

const Modal = styled.div`
    position: fixed;
    top: 50%;
    left: 50%;
    text-align: center;
    transform: translate(-50%, -50%);
    background-color: white;
    width: 500px;
    height: 200px;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    z-index: 9999;
`;
