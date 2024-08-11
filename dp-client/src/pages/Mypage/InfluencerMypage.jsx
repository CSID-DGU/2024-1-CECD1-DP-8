import React, { useState } from 'react';
import InfluencerNavbar from '../../components/Navbar/InfluencerNavbar';
import { styled } from 'styled-components';

const user = {
    id: 'user123',
    password: '1111',
    categories: ['뷰티', '일상']
};

const categoryColor = {
    뷰티: '#FCA5A5',
    패션: '#FCE9A5',
    스포츠: 'lightblue',
    음식: '#3357FF',
    여행: '#FF33A5',
    일상: '#00AAAA'
  };

export default function InfluencerMypage() {
    const [currentPassword, setCurrentPassword] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmNewPassword, setConfirmNewPassword] = useState('');
    const [categories, setCategories] = useState(user.categories || []);
    const [availableCategories, setAvailableCategories] = useState(['뷰티', '일상', '패션', '스포츠', '음식', '여행'].filter(cat => !user.categories.includes(cat)));
    const [message, setMessage] = useState('');

    const handlePasswordChange = (e) => setCurrentPassword(e.target.value);
    const handleNewPasswordChange = (e) => setNewPassword(e.target.value);
    const handleConfirmNewPasswordChange = (e) => setConfirmNewPassword(e.target.value);

    const handleAddCategory = (category) => {
        if (!categories.includes(category)) {   // 자신에게 없는 카테고리 추가
            setCategories([...categories, category]);
            setAvailableCategories(availableCategories.filter((cat) => cat !== category));
        }
    };

    const handleRemoveCategory = (category) => {
        setCategories(categories.filter((cat) => cat !== category));
        setAvailableCategories([...availableCategories, category]);
    };

    const handleSave = () => {
        if (currentPassword == '') {
            setMessage('기존 비밀번호를 입력해 주세요.');
            return;
        }
        if (currentPassword !== user.password) {
            setMessage('현재 비밀번호가 틀립니다.');
            return;
        }
        if (newPassword !== confirmNewPassword) {
            setMessage('새 비밀번호 입력이 같지 않습니다.');
            return;
        }

        // 백엔드 처리 추가해야됨
        const userData = {
            id: user.id,
            newPassword: newPassword,
            categories: categories
        };
        const jsonData = JSON.stringify(userData);
        setMessage(`저장 완료!-> ${jsonData}`);
    };

    return (
        <>
            <Wrapper>
                <InfluencerNavbar></InfluencerNavbar>
                <Container>
                    <FormTitle>설정</FormTitle>
                    <Form>
                        <Label>아이디</Label>
                        <Input type="text" value={user.id} readOnly></Input>
                        <Label>기존 비밀번호</Label>
                        <Input type="password" value={currentPassword} onChange={handlePasswordChange} placeholder="기존 비밀번호를 입력하세요."></Input>
                        (기존비밀번호1111) {currentPassword}
                        <Label>새 비밀번호</Label>
                        <Input type="password" value={newPassword} onChange={handleNewPasswordChange} placeholder="새 비밀번호를 입력하세요."></Input>
                        <Label>새 비밀번호 확인</Label>
                        <Input type="password" value={confirmNewPassword} onChange={handleConfirmNewPasswordChange} placeholder="새 비밀번호를 다시 한번 입력하세요."></Input>
                        <Label>나의 카테고리</Label>
                        <ButtonList>
                            {categories.map((category) => (
                                <CategoryButton key={category} category={category}>
                                    {category} <DeleteButton onClick={() => handleRemoveCategory(category)}>x</DeleteButton>
                                </CategoryButton>
                            ))}
                        </ButtonList>
                        <Label>카테고리 추가</Label>
                        <ButtonList>
                            {availableCategories.map((category) => (
                                <CategoryButton type="button" key={category} category={category} onClick={() => handleAddCategory(category)}>
                                    {category}
                                </CategoryButton>
                            ))}
                        </ButtonList>
                        <BottomArea>
                            {JSON.stringify(categories)}
                            <SubmitButton onClick={handleSave}>저장
                            </SubmitButton>
                            {message && <p>{message}</p>}
                        </BottomArea>
                    </Form>
                </Container>
            </Wrapper>
        </>
    );
}

const Wrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 48px;
`;

const Container = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 33px;
    padding-bottom: 70px;
`;

const FormTitle = styled.div`
    align-self: stretch;
    color: var(--Primary-Navy, #092C4C);
    font-family: Inter;
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 125% */
`;

const Form = styled.div`
    display: flex;
    padding: 27px 20px;
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
    border-radius: var(--20, 20px);
    background: var(--white-100, #FFF);
`;

const Label = styled.div`
    display: flex;
    width: 556px;
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
    align-self: stretch;
    color: var(--Primary-Navy, #092C4C);
    /* Body/Bold */
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 187.5% */
`;

const Input = styled.input`
    display: flex;
    //height: 49px;
    padding: 10px 20px;
    align-items: center;
    gap: 12px;
    align-self: stretch;
    border-radius: var(--8, 8px);
    border: 1px solid var(--Grey-Grey-30, #EAEEF4);
    background: var(--Grey-Grey-10, #F6FAFD);
`;

const ButtonList = styled.div`
    display: flex;
    align-items: flex-start;
    gap: 13px;
    width: 100%;
`;

const CategoryButton = styled.div`
    display: flex;
    padding: 10px;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex-shrink: 0;
    border-radius: var(--20, 20px);
    background: ${(props) => (categoryColor[props.category] || "white")};
    color: #000;
    font-family: Inter;
    font-size: 15px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const DeleteButton = styled.button`
    background-color: transparent;
    border: none;
    font-size: 16px;
    cursor: pointer;
    line-height: 1;
    color: #333;

    &:hover {
        color: red;
    }
`;

const BottomArea = styled.div`
    display: flex;
    flex-direction: column;
    width: 556px;
    height: 77px;
    justify-content: center;
    align-items: center;
    gap: var(--16, 16px);
    padding-top: 30px;
`;

const SubmitButton = styled.button`
    display: flex;
    width: 120px;
    padding: 10px 24px;
    justify-content: center;
    align-items: center;
    gap: 16px;
    flex-shrink: 0;
    border-radius: 70px;
    background: var(--Primary-Blue, #514EF3);
    color: var(--Primary-White, var(--white-100, #FFF));
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 187.5% */
`

const ButtonText = styled.text`
    color: var(--Primary-White, var(--white-100, #FFF));
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 187.5% */
`;