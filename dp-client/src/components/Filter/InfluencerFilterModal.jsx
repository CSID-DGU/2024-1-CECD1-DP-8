import React, { useState, useEffect }  from 'react';
import { styled } from 'styled-components';

export default function InfluencerFilterModal({ setModalOpen, filters, setFilters }) {
    const [beauty, setBeauty] = useState(false);
    const [fashion, setFashion] = useState(false);
    const [sports, setSports] = useState(false);
    const [minFollower, setMinFollower] = useState(0);
    const [maxFollower, setMaxFollower] = useState(0);
    const [maxImpactScore, setMaxImpactScore] = useState(0);
    const [minImpactScore, setMinImpactScore] = useState(0);
    const [gender, setGender] = useState('unset');
    const [hashtagInput, sethashTagInput] = useState('');

    // 모달이 열릴 때 전달받은 필터 값으로 초기화
    useEffect(() => {
        setBeauty(filters.beauty);
        setFashion(filters.fashion);
        setSports(filters.sports);
        setMinFollower(filters.minFollower);
        setMaxFollower(filters.maxFollower);
        setMinImpactScore(filters.minImpactScore);
        setMaxImpactScore(filters.maxImpactScore);
        setGender(filters.gender);
        sethashTagInput(filters.hashtagInput);
    }, [filters]);

    const closeModal = () => {
        setModalOpen(false);
    };

    const handleBeautyClick = () => {
        setBeauty(!beauty);
    }
    const handleFashionClick = () => {
        setFashion(!fashion);
    }
    const handleSportsClick = () => {
        setSports(!sports);
    }

    // 확인 버튼을 눌렀을 때 부모 컴포넌트에 필터 상태 전달
    const handleConfirm = () => {
        setFilters({
            beauty,
            fashion,
            sports,
            minFollower,
            maxFollower,
            minImpactScore,
            maxImpactScore,
            gender,
            hashtagInput
        });
        closeModal();   // 모달 닫기
    };

    return (
        <Container>
            <Title>
                <TitleText>필터 & 키워드 추가</TitleText>
            </Title>
            <Form>
                <FormGroup>
                    <Label>카테고리</Label>
                    <ButtonGroup>
                        <CategoryButton selected={beauty} onClick={handleBeautyClick}>
                            <CategoryButtonText selected={beauty}>뷰티</CategoryButtonText>
                        </CategoryButton>
                        <CategoryButton selected={fashion} onClick={handleFashionClick}>
                            <CategoryButtonText selected={fashion}>패션</CategoryButtonText>
                        </CategoryButton>
                        <CategoryButton selected={sports} onClick={handleSportsClick}>
                            <CategoryButtonText selected={sports}>스포츠</CategoryButtonText>
                        </CategoryButton>
                    </ButtonGroup>
                </FormGroup>
                <FormGroup>
                    <Label>팔로워 수</Label>
                    <InputGroup>
                        <InputField type="text" placeholder="최소 팔로워" value={minFollower} onChange={(e) => setMinFollower(e.target.value)}/>
                        ~
                        <InputField type="text" placeholder="최대 팔로워" value={maxFollower} onChange={(e) => setMaxFollower(e.target.value)}/>
                    </InputGroup>
                </FormGroup>
                <FormGroup>
                    <Label>영향력 지수</Label>
                    <InputGroup>
                        <InputField type="text" placeholder="0" value={minImpactScore} onChange={(e) => setMinImpactScore(e.target.value)}/>
                        ~
                        <InputField type="text" placeholder="100" value={maxImpactScore} onChange={(e) => setMaxImpactScore(e.target.value)}/>
                    </InputGroup>
                </FormGroup>
                <FormGroup>
                    <Label>인플루언서 성별</Label>
                        <SelectField value={gender} onChange={(e) => setGender(e.target.value)}>
                            <option value="unset">설정 안함</option>
                            <option value="female">여자</option>
                            <option value="male">남자</option>
                        </SelectField>
                </FormGroup>
                <FormGroup>
                    <Label>키워드 #해시태그 로 추가</Label>
                    <HashTagInputField
                        type="text"
                        value={hashtagInput}
                        onChange={(e) => sethashTagInput(e.target.value)}
                        placeholder="해시태그 형식으로 입력하세요! 예: #세럼 #물광"
                    />
                    <p>동작확인용(지울예정): {hashtagInput}</p>
                </FormGroup>
            </Form>
            <Action>
                    <ActionButton onClick={closeModal}><ActionButtonText>취소</ActionButtonText></ActionButton>
                    <ActionButton background="var(--primary-blue)" onClick={handleConfirm}><ActionButtonText color="white">확인</ActionButtonText></ActionButton>
            </Action>
        </Container>
    );
}

const Container = styled.div`
    display: flex;
    width: 620px;
    height: 823px;
    flex-direction: column;
    align-items: flex-start;
    border-radius: 12px;
    background: var(--white-100, #FFF);

    position: fixed;
    top: 50%;
    left: 50%;

    transform: translate(-50%, -50%);
    z-index: 9999;

    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
`;

const Title = styled.div`
    display: flex;
    padding: 14px 14px 14px 32px;
    align-items: center;
    gap: 14px;
    align-self: stretch;
    border-bottom: 1px solid var(--background-3, #D0D0D0);
`;

const TitleText = styled.text`
    flex: 1 0 0;
    color: var(--Primary-Navy, #092C4C);
    font-family: Inter;
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 125% */
`;

const Form = styled.div`
    display: flex;
    padding: var(--28, 28px) 32px var(--24, 24px) 32px;
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
    align-self: stretch;

    //스크롤
    overflow-y: scroll;
    //스크롤 투명
    -ms-overflow-style: none;
    scrollbar-width: none;
    ::-webkit-scrollbar {
        display: none;
    }
`;

const FormGroup = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
    align-self: stretch;
`;

const Label = styled.text`
    align-self: stretch;
    color: var(--Primary-Navy, #092C4C);
    /* Body/Bold */
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 187.5% */
`;

const ButtonGroup = styled.div`
    display: flex;
    align-items: flex-start;
    gap: 12px;
`;

const CategoryButton = styled.button`
    display: flex;
    height: 50px;
    padding: 10px 24px;
    justify-content: center;
    align-items: center;
    gap: 16px;
    border-radius: 70px;
    background: var(--Primary-Blue, #514EF3);
    background: ${(props) => (props.selected ? '#FCA5A5' : 'var(--Primary-Blue, #514EF3)')};
    border: transparent;
    box-shadow: ${(props) => (props.selected ? '0px 4px 4px 0px rgba(0, 0, 0, 0.5) inset' : '0px 4px 4px 0px rgba(0, 0, 0, 0.25)')};

    // 버튼이 눌렸을 때의 스타일
    cursor: pointer;
    transition: all 0.3s ease;
    &:active {
        background-color: #2980b9; // 버튼이 눌렸을 때 배경색 변경
        transform: translateY(2px); // 버튼이 눌렀을 때 아래로 이동
        box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.5) inset;
    }
`;

const CategoryButtonText = styled.text`
    color: ${(props) => (props.selected ? '#000000' : '#FFFFFF')};
    /* Small/Medium */
    font-family: Inter;
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: 30px; /* 214.286% */
`;

const InputGroup = styled.div`
    display: flex;
    align-items: flex-start;
    gap: 20px;
    align-self: stretch;
`;

const InputField = styled.input`
    width: 122px;
    height: 50px;
    padding: 0 20px;
    border-radius: 8px;
    border: 1px solid var(--Grey-Grey-30, #EAEEF4);
    background: var(--Grey-Grey-10, #F6FAFD);
`;

const SelectField = styled.select`
    width: 150px;
    padding: 10px 20px;
    border-radius: 8px;
    border: 1px solid var(--Grey-Grey-30, #EAEEF4);
    background: var(--Grey-Grey-10, #F6FAFD);
`;

const HashTagInputField = styled.textarea`
    width: 500px;
    height: 150px;
    padding: 10px 20px;
    border-radius: var(--8, 8px);
    border: 1px solid var(--Grey-Grey-30, #EAEEF4);
    background: var(--Grey-Grey-10, #F6FAFD);
`;

const Action = styled.div`
    display: flex;
    justify-content: flex-end;
    padding: var(--16, 16px) 32px var(--28, 28px) 32px;
    align-items: center;
    gap: 10px;
    align-self: stretch;
    border-top: 1px solid #DDD;
`;

const ActionButton = styled.button`
    display: flex;
    width: 120px;
    padding: 10px 24px;
    justify-content: center;
    align-items: center;
    gap: 16px;
    border-radius: 70px;
    border: transparent;
    background: ${(props) => props.background || "white"};
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);

    cursor: pointer;
    transition: all 0.3s ease;

    // 버튼이 눌렸을 때의 스타일
    &:active {
        background-color: #2980b9; // 버튼이 눌렸을 때 배경색 변경
        transform: translateY(2px); // 버튼을 눌렀을 때 아래로 이동
        box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.5);
    }
`;

const ActionButtonText = styled.text`
    color: ${(props) => (props.color === 'white' ? 'white' : 'black')};
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px; /* 187.5% */
`;