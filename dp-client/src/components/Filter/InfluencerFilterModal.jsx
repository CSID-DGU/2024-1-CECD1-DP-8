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
        { id: 'sports', label: '스포츠', color: '#86EFAC' },
        { id: 'homeLiving', label: '홈 / 리빙', color: '#E9D5FF' },
        { id: 'music', label: '음악', color: '#BAE6FD' },
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
                        <Label>키워드 #해시태그 로 추가</Label>
                        <TextArea
                            placeholder="해시태그 형식으로 입력하세요! 예: #뷰티 #패션"
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

const ModalContainer = styled.div`
    width: 600px;
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const ModalHeader = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background: #f5f5f5;
    border-bottom: 1px solid #ddd;
`;

const HeaderTitle = styled.h2`
    font-size: 20px;
    margin: 0;
`;

const CloseButton = styled.button`
    background: none;
    border: none;
    font-size: 18px;
    cursor: pointer;
`;

const ModalContent = styled.div`
    padding: 20px;
`;

const FormGroup = styled.div`
    margin-bottom: 20px;
`;

const Label = styled.label`
    display: block;
    font-size: 14px;
    margin-bottom: 8px;
    font-weight: bold;
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
    font-size: 15px;
    width: 91.478px;
    height: 35px;
    padding: 10px;
    gap: 10px;
    border-radius: 20px;
    border: none;
    background: ${(props) => (props.selected ? props.color : '#f1f1f1')};
    color: ${(props) => (props.selected ? 'white' : 'black')};
    cursor: pointer;
    box-shadow: ${(props) => (props.selected ? '0px 4px 8px rgba(0, 0, 0, 0.15)' : '0px 2px 4px rgba(0, 0, 0, 0.1)')};
    transition: all 0.3s ease;

    &:hover {
        background: ${(props) => props.color};
        color: white;
    }
`;

const FollowerInputContainer = styled.div`
    display: flex;
    width: 100px;
    gap: 12px;
`;

const InputField = styled.input`
    width: 120px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 20px;
`;

const SelectField = styled.select`
    width: 100%;
    padding: 8px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
`;

const TextArea = styled.textarea`
    width: 100%;
    height: 80px;
    padding: 8px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
`;

const ErrorText = styled.p`
    color: red;
    font-size: 14px;
    margin-top: -10px;
    margin-bottom: 20px;
`;

const ModalFooter = styled.div`
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    padding: 20px;
    background: #f5f5f5;
    border-top: 1px solid #ddd;
`;

const FooterButton = styled.button`
    display: flex;
    width: 60px;
    height: 35px;
    justify-content: center;
    align-items: center;
    gap: 16px;
    font-size: 10px;
    background: ${(props) => (props.primary ? '#8a54ff' : '#f1f1f1')};
    color: ${(props) => (props.primary ? 'white' : 'black')};
    border: none;
    border-radius: 70px;
    cursor: pointer;
`;
