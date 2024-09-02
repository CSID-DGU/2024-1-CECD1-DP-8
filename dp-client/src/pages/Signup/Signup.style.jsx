import styled from 'styled-components';
import { IoEye } from 'react-icons/io5';
import { IoEyeOff } from 'react-icons/io5';

export const SignupSection = styled.div`
    display: flex;
    width: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
`;

export const SignupContent = styled.div`
    display: flex;
    width: 1260px;
    padding: 10px 0px;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
`;

export const SignupPane = styled.div`
    display: flex;
    width: 630px;
    padding: 50px 10px;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
    align-self: stretch;
`;

export const SignupForm = styled.div`
    display: flex;
    padding: 0px 30px;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    flex: 1 0 0;
    align-self: stretch;
`;

export const FormContainer = styled.div`
    display: flex;
    width: 384px;
    height: 100%;
    flex-direction: column;
    align-items: flex-start;
    gap: 60px;
`;

export const SignupTitle = styled.div`
    align-self: stretch;
    color: var(--Color-Text-primary, #222);
    margin-bottom: 32px;

    /* ST1_SB */
    font-family: Pretendard;
    font-size: var(--Text-size-7, 22px);
    font-style: normal;
    font-weight: 600;
    line-height: 140%; /* 30.8px */
    letter-spacing: -0.44px;
`;

export const Frame = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--Spacing-6, 32px);
    align-self: stretch;
`;

export const SignupContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: var(--Spacing-3, 8px);
    align-self: stretch;
`;

export const Button = styled.button`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    align-self: stretch;
    border-radius: 3px;
    background: var(--Color-Main-primary, #65bd83);
`;

export const SignupText = styled.div`
    display: flex;
    padding: 16px 151px;
    justify-content: center;
    align-items: center;
    gap: var(--Spacing-2, 6px);
    align-self: stretch;
    color: #ffffff;
    white-space: nowrap;
`;

export const Form = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: var(--Spacing-6, 32px);
    align-self: stretch;
`;

export const InputContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: var(--Spacing-3, 8px);
    align-self: stretch;
`;

export const InputType = styled.div`
    align-self: stretch;
    color: var(--Color-Text-primary, #222);

    /* B1_SB */
    font-family: Pretendard;
    font-size: var(--Text-size-5, 18px);
    font-style: normal;
    font-weight: 600;
    line-height: 140%; /* 25.2px */
    letter-spacing: -0.36px;
`;

export const InputField = styled.div`
    display: flex;
    padding: 18px 24px;
    justify-content: center;
    align-items: center;
    gap: 10px;
    align-self: stretch;
    border-radius: 10px;
    border: 1px solid var(--Color-Gray-gray-600, #757575);
`;

export const Input = styled.input`
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex: 1 0 0;
    border: 0px;
    width: 255px;
    height: 22px;
`;

export const Cause = styled.div`
    align-self: stretch;
    color: var(--Color-Text-secondary, #616161);

    /* B7_R */
    font-family: Pretendard;
    font-size: var(--Text-size-3, 14px);
    font-style: normal;
    font-weight: 400;
    line-height: 140%; /* 19.6px */
    letter-spacing: -0.28px;
`;

export const StyledIcon = styled(IoEye)`
    width: var(--Text-size-7, 22px);
    height: var(--Text-size-7, 22px);
    flex-shrink: 0;
    opacity: 0.5;
`;

export const StyledIcon2 = styled(IoEyeOff)`
    width: var(--Text-size-7, 22px);
    height: var(--Text-size-7, 22px);
    flex-shrink: 0;
    opacity: 0.5;
`;

export const Agree = styled.div`
    display: flex;
    align-items: center;
    gap: var(--Spacing-1, 4px);
`;

export const AgreeText = styled.div`
    color: var(--Color-Text-primary, #222);

    /* B6_M */
    font-family: Pretendard;
    font-size: var(--Text-size-3, 14px);
    font-style: normal;
    font-weight: 500;
    line-height: 140%; /* 19.6px */
    letter-spacing: -0.28px;
`;

export const Checkbox = styled.input`
    width: var(--Text-size-6, 20px);
    height: var(--Text-size-6, 20px);
    accent-color: black;
`;

export const Warn = styled.div`
    align-self: stretch;
    color: var(--Color-Semantic-warning, #ff616a);

    /* B6_M */
    font-family: Pretendard;
    font-size: var(--Text-size-3, 14px);
    font-style: normal;
    font-weight: 500;
    line-height: 140%; /* 19.6px */
    letter-spacing: -0.28px;
`;

export const UserType = styled.div`
    display: flex;
    width: 298px;
    padding: var(--Spacing-2, 6px);
    align-items: center;
    border-radius: 100px;
    background: var(--Color-Gray-gray-200, #eee);
`;

export const UserTypeButton = styled.button`
    display: flex;
    width: 143px;
    padding: var(--Text-size-2, 12px) var(--Spacing-4, 16px);
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex-shrink: 0;
    border-radius: 100px;

    /* B3_SB */
    font-family: Pretendard;
    font-size: var(--Text-size-4, 16px);
    font-style: normal;
    font-weight: 600;
    line-height: 140%; /* 22.4px */
    letter-spacing: -0.32px;
`;

export const OkButton = styled.button`
    display: flex;
    padding: 6px 10px;
    flex-direction: column;
    align-items: flex-start;
    gap: var(--Spacing-2, 6px);
    border-radius: 3px;
    background: var(--Color-Main-primary, #65bd83);
`;

export const OkbuttonLayer = styled.div`
    color: #fff;
    font-family: Pretendard;
    font-size: var(--Text-size-3, 14px);
    font-style: normal;
    font-weight: 600;
    line-height: 140%; /* 19.6px */
    letter-spacing: -0.28px;
    white-space: nowrap;
`;
