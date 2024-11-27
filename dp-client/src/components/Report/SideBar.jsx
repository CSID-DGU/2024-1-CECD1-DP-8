import React from 'react';
import styled from 'styled-components';

export default function SideBar({ profile, selectedPage, setSelectedPage }) {
    return (
        <SidebarWrapper>
            <ProfileImage>
                <img src={profile.profilePictureUrl} alt="프로필" />
            </ProfileImage>
            <Username>@{profile.nickname}</Username>
            <Name>{profile.name}</Name>
            <Category>{profile.category}</Category>
            <ProfileData>
                <ProfileDataItem>
                    <DataValue>{profile.mediaCnt.toLocaleString()}</DataValue>
                    <DataLabel>게시글</DataLabel>
                </ProfileDataItem>
                <ProfileDataItem>
                    <DataValue>{profile.followerCnt.toLocaleString()}</DataValue>
                    <DataLabel>팔로워</DataLabel>
                </ProfileDataItem>
            </ProfileData>
            <ButtonWrapper>
                <Button isSelected={selectedPage === 'postAnalysis'} onClick={() => setSelectedPage('postAnalysis')}>
                    포스트 분석
                </Button>
                <Button
                    isSelected={selectedPage === 'hashtagAnalysis'}
                    onClick={() => setSelectedPage('hashtagAnalysis')}
                >
                    해시태그 분석
                </Button>
            </ButtonWrapper>
        </SidebarWrapper>
    );
}

const SidebarWrapper = styled.div`
    width: 282px;
    padding: 20px;
    border-radius: 20px;
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;

    @media (max-width: 768px) {
        width: 100%;
        height: auto;
        padding: 16px;
    }
`;

const ProfileImage = styled.div`
    margin-top: 50px;
    width: 170px;
    height: 170px;
    border-radius: 50%;
    background: linear-gradient(45deg, #ffdc80, #fcb045, #fd1d1d, #833ab4, #5851db);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: center;

    img {
        width: 160px;
        height: 160px;
        border-radius: 50%;
        border: 2px solid white;
    }

    @media (max-width: 768px) {
        margin-top: 20px;
        width: 130px;
        height: 130px;

        img {
            width: 120px;
            height: 120px;
        }
    }
`;

const Username = styled.p`
    font-family: Inter;
    font-size: 20px;
    font-weight: 600;
    margin-top: 10px;

    @media (max-width: 768px) {
        font-size: 18px;
    }
`;

const Name = styled.p`
    font-size: 18px;
    font-weight: 500;
    margin: 5px 0;

    @media (max-width: 768px) {
        font-size: 16px;
    }
`;

const Category = styled.p`
    font-size: 16px;
    font-weight: 400;
    color: #666;
    margin-bottom: 20px;

    @media (max-width: 768px) {
        font-size: 14px;
    }
`;

const ProfileData = styled.div`
    display: flex;
    justify-content: space-around;
    width: 100%;
    margin: 20px 0;
    padding: 20px;

    @media (max-width: 768px) {
        flex-direction: column;
        align-items: center;
        padding: 12px;
    }
`;

const ProfileDataItem = styled.div`
    text-align: center;
    margin-bottom: 10px;

    @media (max-width: 768px) {
        margin-bottom: 8px;
    }
`;

const DataValue = styled.p`
    font-size: 18px;
    font-weight: 600;

    @media (max-width: 768px) {
        font-size: 16px;
    }
`;

const DataLabel = styled.p`
    font-size: 14px;
    font-weight: 400;
    color: #666;

    @media (max-width: 768px) {
        font-size: 12px;
    }
`;

const ButtonWrapper = styled.div`
    display: flex;
    flex-direction: column;
    gap: 10px;
`;

const Button = styled.button`
    background: ${(props) =>
        props.isSelected
            ? 'linear-gradient(90deg, rgba(74, 58, 255, 0.80) 0%, rgba(102, 48, 170, 0.80) 100%)'
            : '#b0b0b0'};
    color: #fff;
    font-size: 16px;
    font-weight: 600;
    padding: 10px 35px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;

    &:hover {
        background: ${(props) =>
            props.isSelected
                ? 'linear-gradient(90deg, rgba(74, 58, 255, 0.9) 0%, rgba(102, 48, 170, 0.9) 100%)'
                : '#808080'};
    }

    @media (max-width: 768px) {
        font-size: 14px;
        padding: 8px 12px;
    }
`;
