import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

export default function InfluencerFilterModal({ setModalOpen, filters, setFilters }) {
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [minFollower, setMinFollower] = useState('');
    const [maxFollower, setMaxFollower] = useState('');
    const [gender, setGender] = useState('unset');
    const [hashtagInput, setHashtagInput] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const categories = [
        { id: 'beauty', label: '뷰티', color: '#FCA5A5' },
        { id: 'fashion', label: '패션', color: '#FDE68A' },
        { id: 'living', label: '일상', color: '#86EFAC' },
        { id: 'travel', label: '여행', color: '#E9D5FF' },
    ];

    useEffect(() => {
        if (filters) {
            setSelectedCategory(filters.selectedCategory || null);
            setMinFollower(filters.minFollower || '');
            setMaxFollower(filters.maxFollower || '');
            setGender(filters.gender || 'unset');
            setHashtagInput(filters.hashtagInput || '');
        }
    }, [filters]);

    const closeModal = () => setModalOpen(false);

    const handleCategoryClick = (categoryId) => {
        // 선택된 카테고리를 다시 누르면 취소
        if (selectedCategory === categoryId) {
            setSelectedCategory(null);
        } else {
            setSelectedCategory(categoryId);
        }
    };

    const validateInputs = () => {
        // 최소/최대 팔로워 값이 숫자인지 확인
        if (minFollower && isNaN(minFollower)) {
            setErrorMessage('최소 팔로워 수는 숫자여야 합니다.');
            return false;
        }
        if (maxFollower && isNaN(maxFollower)) {
            setErrorMessage('최대 팔로워 수는 숫자여야 합니다.');
            return false;
        }
        // 최소값이 최대값보다 크지 않은지 확인
        if (minFollower && maxFollower && Number(minFollower) > Number(maxFollower)) {
            setErrorMessage('최소 팔로워 수는 최대 팔로워 수보다 작아야 합니다.');
            return false;
        }
        // 카테고리가 선택되지 않았을 경우
        if (!selectedCategory) {
            setErrorMessage('카테고리를 하나 이상 선택해주세요.');
            return false;
        }
        setErrorMessage(''); // 모든 유효성 검사가 통과되면 에러 메시지 초기화
        return true;
    };

    const handleConfirm = () => {
        if (validateInputs()) {
            setFilters({
                selectedCategory,
                minFollower,
                maxFollower,
                gender,
                hashtagInput,
            });
            closeModal();
        }
    };

    return (
        <ModalOverlay>
            <ModalContainer>
                <ModalHeader>
                    <HeaderTitle>필터 & 키워드 추가</HeaderTitle>
                    <CloseButton onClick={closeModal}>✕</CloseButton>
                </ModalHeader>
                <ModalContent>
                    <FormGroup>
                        <Label>카테고리</Label>
                        <CategoryContainer>
                            {categories.map((category) => (
                                <CategoryButton
                                    key={category.id}
                                    selected={selectedCategory === category.id}
                                    color={category.color}
                                    onClick={() => handleCategoryClick(category.id)}
                                >
                                    {category.label}
                                </CategoryButton>
                            ))}
                        </CategoryContainer>
                    </FormGroup>
                    <FormGroup>
                        <Label>팔로워 수</Label>
                        <FollowerInputContainer>
                            <InputField
                                placeholder="최소 팔로워"
                                value={minFollower}
                                onChange={(e) => setMinFollower(e.target.value)}
                            />
                            <span>~</span>
                            <InputField
                                placeholder="최대 팔로워"
                                value={maxFollower}
                                onChange={(e) => setMaxFollower(e.target.value)}
                            />
                        </FollowerInputContainer>
                    </FormGroup>
                    <FormGroup>
                        <Label>인플루언서 성별</Label>
                        <SelectField value={gender} onChange={(e) => setGender(e.target.value)}>
                            <option value="unset">선택 안함</option>
                            <option value="female">여자</option>
                            <option value="male">남자</option>
                        </SelectField>
                    </FormGroup>
                    <FormGroup>
                        <Label>원하는 키워드 추가</Label>
                        <TextArea
                            placeholder="예: 일상정보, 릴스, 토너패트"
                            value={hashtagInput}
                            onChange={(e) => setHashtagInput(e.target.value)}
                        />
                    </FormGroup>
                    {errorMessage && <ErrorText>{errorMessage}</ErrorText>}
                </ModalContent>
                <ModalFooter>
                    <FooterButton onClick={closeModal}>취소</FooterButton>
                    <FooterButton primary onClick={handleConfirm}>
                        적용
                    </FooterButton>
                </ModalFooter>
            </ModalContainer>
        </ModalOverlay>
    );
}
const ModalContainer = styled.div`
    width: 600px;
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    animation: fadeIn 0.3s ease-in-out;

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;

const ModalHeader = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background: linear-gradient(90deg, #aa96fc 0%, #463392 100%);
    color: white;
`;

const HeaderTitle = styled.h2`
    font-size: 22px;
    margin: 0;
    font-weight: bold;
`;

const CloseButton = styled.button`
    background: transparent;
    border: none;
    font-size: 18px;
    color: white;
    cursor: pointer;
    transition: transform 0.2s;

    &:hover {
        transform: rotate(90deg);
    }
`;

const ModalContent = styled.div`
    padding: 20px;
`;

const FormGroup = styled.div`
    margin-bottom: 20px;

    label {
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 8px;
        display: block;
        color: #333;
    }
`;

const CategoryContainer = styled.div`
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
`;

const CategoryButton = styled.button`
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 14px;
    padding: 10px 16px;
    border-radius: 24px;
    border: 1px solid ${(props) => (props.selected ? props.color : '#ddd')};
    background: ${(props) => (props.selected ? props.color : 'white')};
    color: ${(props) => (props.selected ? 'white' : '#333')};
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;

    &:hover {
        background: ${(props) => props.color};
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
`;

const InputField = styled.input`
    width: calc(50% - 10px);
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.2s;

    &:focus {
        border-color: #463392;
        outline: none;
        box-shadow: 0 0 4px rgba(70, 51, 146, 0.3);
    }
`;

const SelectField = styled.select`
    width: 100%;
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.2s;

    &:focus {
        border-color: #463392;
        outline: none;
        box-shadow: 0 0 4px rgba(70, 51, 146, 0.3);
    }
`;

const TextArea = styled.textarea`
    width: 100%;
    height: 100px;
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.2s;

    &:focus {
        border-color: #463392;
        outline: none;
        box-shadow: 0 0 4px rgba(70, 51, 146, 0.3);
    }
`;

const FooterButton = styled.button`
    padding: 12px 24px;
    border-radius: 24px;
    border: none;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    background: ${(props) => (props.primary ? '#463392' : '#ddd')};
    color: ${(props) => (props.primary ? 'white' : '#333')};

    &:hover {
        background: ${(props) => (props.primary ? '#301f72' : '#ccc')};
        transform: scale(1.05);
    }
`;

const ErrorText = styled.p`
    color: red;
    font-size: 14px;
    margin: 10px 0;
    animation: shake 0.3s;

    @keyframes shake {
        0%,
        100% {
            transform: translateX(0);
        }
        25% {
            transform: translateX(-4px);
        }
        75% {
            transform: translateX(4px);
        }
    }
`;

const ModalOverlay = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
`;

const Label = styled.label`
    display: block;
    font-size: 14px;
    margin-bottom: 8px;
    font-weight: bold;
`;

const FollowerInputContainer = styled.div`
    display: flex;
    width: 300px;
    gap: 12px;
    height: 40px;
`;

const ModalFooter = styled.div`
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    padding: 20px;
    background: #f5f5f5;
    border-top: 1px solid #ddd;
`;
