import { Link, useNavigate, useLocation } from 'react-router-dom';
import {
    SignupContent,
    SignupSection,
    SignupPane,
    SignupForm,
    FormContainer,
    SignupTitle,
    Frame,
    SignupContainer,
    Button,
    Form,
    InputContainer,
    InputType,
    InputField,
    Input,
    Cause,
    StyledIcon,
    StyledIcon2,
    Agree,
    AgreeText,
    Checkbox,
    SignupText,
    Warn,
    UserType,
    UserTypeButton,
    OkButton,
    OkbuttonLayer,
} from './Signup.style';
import { useState, useEffect } from 'react';
import { loginData } from '../../store/userSlice';
import axios from 'axios';
import { postData } from '../../services/api';

export default function SingUp() {
    const navigate = useNavigate();
    const location = useLocation();
    const [loading, setLoading] = useState('');
    const [activeButton, setActiveButton] = useState('Consumer');
    const [showPassword, setShowPassword] = useState(false);
    const [showPassword2, setShowPassword2] = useState(false);
    const [click, setClick] = useState(false);

    //body에 입력되는 state
    const [nickname, setNickname] = useState('');
    const [email, setEmail] = useState('');
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    //버튼 활성화 위한 state
    const [nicknameCheck, setNicknameCheck] = useState(false);
    const [emailCheck, setEmailCheck] = useState(false);
    const [idCheck, setIdCheck] = useState(false);
    const [passwordCheck, setPasswordCheck] = useState(false);
    const [password2Check, setPassword2Check] = useState(false);
    const [btn, setBtn] = useState(false);

    //wanr 메시지를 위한 state
    const [nicknameMessage, setNicknameMessage] = useState('');
    const [emailMessage, setEmailMessage] = useState('');
    const [idMessage, setIdMessage] = useState('');
    const [passwordMessage, setPasswordMessage] = useState('');
    const [password2Message, setPassword2Message] = useState('');

    //focus 확인을 위한 state
    const [passwordFocus, setPasswordFocus] = useState(false);
    const [password2Focus, setPassword2Focus] = useState(false);

    //check 확인을 위한 state
    const [isChecked, setIsChecked] = useState(false);

    //닉네임 유효성 검사
    const checkNickname = (value) => {
        const regExp = /^[a-zA-Z가-힣0-9]*$/;
        setNickname(value);

        if (value.trim() === '') {
            setNicknameMessage('닉네임을 입력해주세요.');
            setNicknameCheck(false);
        } else if (!regExp.test(value)) {
            setNicknameMessage('문자로 입력해주세요.');
            setNicknameCheck(false);
        } else {
            setNicknameMessage('');
            setNicknameCheck(true);
        }
    };

    //이메일 유효성 검사
    const checkEmail = (value) => {
        //영어 소문자, 숫자, @와 .을 포함
        const regExp = /^[a-z0-9]+@[a-z0-9]+\.[a-z]+$/;
        setEmail(value);

        if (value.trim() === '') {
            setEmailMessage('이메일을 입력해주세요.');
            setEmailCheck(false);
        } else if (!regExp.test(value)) {
            setEmailMessage('유효하지 않은 이메일 형식입니다.');
            setEmailCheck(false);
        } else {
            setEmailMessage('');
            setEmailCheck(true);
        }
    };

    //아이디 유효성 검사
    const checkId = (value) => {
        // 영문과 숫자를 포함하고 8자 이상
        const regExp = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;

        setId(value);

        if (value.trim() === '') {
            setIdMessage('아이디를 입력해주세요.');
            setIdCheck(false);
        } else if (value.length < 8) {
            setIdMessage('최소 8자리 이상 입력해주세요.');
            setIdCheck(false);
        } else if (!regExp.test(value)) {
            setIdMessage('아이디는 영문과 숫자를 포함해야 합니다.');
            setIdCheck(false);
        } else {
            setIdMessage('');
            setIdCheck(true);
        }
    };

    //비밀번호 유효성 검사
    const checkPassword = (value) => {
        // 영문과 숫자를 포함하고 8자 이상
        const regExp = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;

        setPassword(value);

        if (value.trim() === '') {
            setPasswordMessage('비밀번호를 입력해주세요.');
            setPasswordCheck(false);
        } else if (value.length < 8) {
            setPasswordMessage('최소 8자리 이상 입력해주세요.');
            setPasswordCheck(false);
        } else if (!regExp.test(value)) {
            setPasswordMessage('비밀번호는 영문과 숫자를 포함해야 합니다.');
            setPasswordCheck(false);
        } else {
            setPasswordMessage('');
            setPasswordCheck(true);
        }
    };

    //비밀번호 확인 유효성 검사
    const checkPassword2 = (value) => {
        setPassword2(value);

        if (value.trim() === '') {
            setPassword2Message('비밀번호를 다시 입력해주세요.');
            setPassword2Check(false);
        } else if (value !== password) {
            setPassword2Message('비밀번호가 일치하지 않습니다.');
            setPassword2Check(false);
        } else {
            setPassword2Message('');
            setPassword2Check(true);
        }
    };

    useEffect(() => {
        const queryParams = new URLSearchParams(location.search);
        const role = queryParams.get('role');
        if (role) {
            setActiveButton(role);
        }
    }, [location.search]);

    useEffect(() => {
        if (nicknameCheck && emailCheck && idCheck && passwordCheck && password2Check) {
            setBtn(true);
        } else {
            setBtn(false);
        }
    }, [nicknameCheck, emailCheck, idCheck, passwordCheck, password2Check]);

    // password가 변경될 때 password2의 유효성을 다시 확인하도록 추가
    useEffect(() => {
        if (password2 !== '') {
            checkPassword2(password2);
        }
    }, [password]);

    const handleSignup = async (e) => {
        e.preventDefault();

        setLoading(true);

        try {
            const body = {
                nickname: nickname,
                email: email,
                password: password,
                loginId: id,
                type: activeButton === 'Consumer' ? 'general' : 'creator',
                status: 'active',
            };

            await postData('/users/signup', body);
            console.log('회원가입 성공');
            navigate('/login');
            loginData(body);
        } catch (error) {
            setLoading(false);
            if (error.response) {
                const errorCode = error.response.data.code;

                //수정 필요
                if (errorCode === 'USER4010') {
                    setIdMessage('이미 가입된 아이디입니다.');
                } else if (errorCode === 'USER4012') {
                    setNicknameMessage('이미 있는 닉네임입니다.');
                } else if (errorCode === 'USER4015') {
                    setEmailMessage('이메일 인증이 완료되지 않았습니다.');
                } else if (errorCode === 'USER4011') {
                    setClick(false);
                    setEmailMessage('이미 가입된 이메일입니다.');
                } else {
                    console.error('알 수 없는 에러 코드:', errorCode);
                }
            }
        }
    };

    const handleButtonClick = (e) => {
        e.preventDefault();

        if (btn && isChecked && click) {
            handleSignup(e);
        } else if (btn && !isChecked) {
            alert('이용약관에 동의해주세요.');
        } else if (btn && !click) {
            setEmailMessage('이메일 인증을 진행해 주세요.');
        } else {
            alert('모든 정보를 빠짐없이 입력해주세요.');
        }
    };

    const handleCheckboxChange = (e) => {
        setIsChecked(e.target.checked);
    };

    const handleVerify = async (e) => {
        e.preventDefault();

        if (emailCheck && !click) {
            try {
                const body = {
                    email: email,
                };

                await postData('/users/email-verification', body);
                setClick(true);
                setEmailMessage('');
                console.log('메일 보내짐');
            } catch (error) {
                if (error.response) {
                    const errorCode = error.response.data.code;

                    //수정 필요
                    if (errorCode === 'USER4011') {
                        setClick(false);
                        setEmailMessage('이미 존재하는 이메일입니다.');
                    } else if (errorCode === 'USER4016') {
                        setClick(false);
                        setEmailMessage('이미 인증된 이메일입니다.');
                    } else if (errorCode === 'USER4014') {
                        setClick(false);
                        setEmailMessage('만료된 이메일 토큰입니다.');
                    } else {
                        console.error('알 수 없는 에러 코드:', errorCode);
                    }
                }
            }
        }
    };

    return (
        <div>
            <SignupSection>
                <SignupContent>
                    <SignupPane>
                        <SignupForm>
                            <FormContainer>
                                <Frame>
                                    <SignupContainer>
                                        <SignupTitle>회원가입</SignupTitle>
                                        <Form>
                                            <InputContainer>
                                                <InputType>닉네임</InputType>
                                                <InputField
                                                    style={{
                                                        border: nicknameMessage
                                                            ? '1px solid #FF616A'
                                                            : '1px solid #757575',
                                                    }}
                                                >
                                                    <Input
                                                        type="text"
                                                        placeholder="닉네임"
                                                        value={nickname}
                                                        onChange={(e) => checkNickname(e.target.value.trim())}
                                                    ></Input>
                                                </InputField>
                                                <Warn>{nicknameMessage}</Warn>
                                            </InputContainer>
                                            <InputContainer>
                                                <InputType>이메일</InputType>
                                                <Cause>인증에 사용할 이메일을 작성해 주세요.</Cause>
                                                <InputField
                                                    style={{
                                                        border: emailMessage
                                                            ? '1px solid #FF616A'
                                                            : '1px solid #757575',
                                                    }}
                                                >
                                                    <Input
                                                        type="email"
                                                        placeholder="ex) example@naver.com"
                                                        value={email}
                                                        onChange={(e) => {
                                                            checkEmail(e.target.value.trim());
                                                            setClick(false);
                                                        }}
                                                    ></Input>
                                                    <OkButton
                                                        onClick={handleVerify}
                                                        style={{
                                                            background: click ? '#00000014' : '#4A3AFF',
                                                        }}
                                                    >
                                                        <OkbuttonLayer style={{ color: click ? '#9E9E9E' : '#FFFFFF' }}>
                                                            {click ? '메일 전송' : '인증 요청'}
                                                        </OkbuttonLayer>
                                                    </OkButton>
                                                </InputField>
                                                <Warn>{emailMessage}</Warn>
                                            </InputContainer>
                                            <InputContainer>
                                                <InputType>아이디</InputType>
                                                <InputField
                                                    style={{
                                                        border: idMessage ? '1px solid #FF616A' : '1px solid #757575',
                                                    }}
                                                >
                                                    <Input
                                                        type="text"
                                                        placeholder="아이디"
                                                        value={id}
                                                        onChange={(e) => checkId(e.target.value.trim())}
                                                    ></Input>
                                                </InputField>
                                                <Warn>{idMessage}</Warn>
                                            </InputContainer>
                                            <InputContainer>
                                                <InputType>비밀번호</InputType>
                                                <Cause>영문, 숫자를 포함한 8자 이상의 비밀번호를 입력해주세요.</Cause>
                                                <InputField
                                                    onFocus={() => {
                                                        setPasswordFocus(true);
                                                    }}
                                                    onBlur={() => {
                                                        setPasswordFocus(false);
                                                    }}
                                                    style={{
                                                        border:
                                                            passwordFocus && passwordCheck
                                                                ? '1px solid #65BD83'
                                                                : passwordMessage
                                                                ? '1px solid #FF616A'
                                                                : '1px solid #757575',
                                                    }}
                                                >
                                                    <Input
                                                        type={showPassword ? 'text' : 'password'}
                                                        placeholder="비밀번호"
                                                        value={password}
                                                        onChange={(e) => {
                                                            checkPassword(e.target.value.trim());
                                                        }}
                                                    ></Input>
                                                    {showPassword ? (
                                                        <StyledIcon2
                                                            onClick={() => setShowPassword(!showPassword)}
                                                        ></StyledIcon2>
                                                    ) : (
                                                        <StyledIcon
                                                            onClick={() => setShowPassword(!showPassword)}
                                                        ></StyledIcon>
                                                    )}
                                                </InputField>
                                                <Warn>{passwordMessage}</Warn>
                                            </InputContainer>
                                            <InputContainer>
                                                <InputType>비밀번호 확인</InputType>
                                                <InputField
                                                    onFocus={() => {
                                                        setPassword2Focus(true);
                                                    }}
                                                    onBlur={() => {
                                                        setPassword2Focus(false);
                                                    }}
                                                    style={{
                                                        border:
                                                            password2Focus && password2Check
                                                                ? '1px solid #65BD83'
                                                                : password2Message
                                                                ? '1px solid #FF616A'
                                                                : '1px solid #757575',
                                                    }}
                                                >
                                                    <Input
                                                        type={showPassword2 ? 'text' : 'password'}
                                                        placeholder="비밀번호 확인"
                                                        value={password2}
                                                        onChange={(e) => {
                                                            checkPassword2(e.target.value.trim());
                                                        }}
                                                    ></Input>
                                                    {showPassword2 ? (
                                                        <StyledIcon2
                                                            onClick={() => setShowPassword2(!showPassword2)}
                                                        ></StyledIcon2>
                                                    ) : (
                                                        <StyledIcon
                                                            onClick={() => setShowPassword2(!showPassword2)}
                                                        ></StyledIcon>
                                                    )}
                                                </InputField>
                                                <Warn>{password2Message}</Warn>
                                            </InputContainer>
                                        </Form>
                                        <Agree>
                                            <Checkbox type="checkbox" onChange={handleCheckboxChange}></Checkbox>
                                            <AgreeText style={{ color: isChecked ? '#65BD83' : '#000' }}>
                                                이용약관, 개인 정보 수집 및 이용에 동의합니다.
                                            </AgreeText>
                                        </Agree>
                                    </SignupContainer>

                                    <Button onClick={handleButtonClick}>
                                        <SignupText>{loading ? 'Loading...' : '회원가입 하기'}</SignupText>
                                    </Button>
                                </Frame>
                            </FormContainer>
                        </SignupForm>
                    </SignupPane>
                </SignupContent>
            </SignupSection>
        </div>
    );
}
