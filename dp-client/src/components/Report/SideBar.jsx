import React, { useState } from 'react';
import styled from 'styled-components';

export default function SideBar({ profile, onSelect }) {
    const [activeButton, setActiveButton] = useState('postAnalysis');

    const handleButtonClick = (button) => {
        setActiveButton(button);
        onSelect(button); // Notify parent component about the selected button
    };

    return (
        <SidebarWrapper>
            <ProfileImage>
                <img src={profile.imageURL} alt="프로필" />
            </ProfileImage>
            <Username>@{profile.nickname}</Username>
            <Name>{profile.name}</Name>
            <Category>{profile.category}</Category>
            <ProfileData>
                <ProfileDataColumn>
                    <ProfileDataItem>
                        <DataValue>{profile.mediaCnt.toLocaleString()}</DataValue>
                        <DataLabel>게시글</DataLabel>
                    </ProfileDataItem>
                    <ProfileDataItem>
                        <DataValue>{profile.followerCnt.toLocaleString()}</DataValue>
                        <DataLabel>팔로워</DataLabel>
                    </ProfileDataItem>
                </ProfileDataColumn>
                <ProfileDataColumn>
                    <ProfileDataItem>
                        <DataValue>{profile.InfluenceIndex.toLocaleString()}</DataValue>
                        <DataLabel>영향력지수</DataLabel>
                    </ProfileDataItem>
                    <ProfileDataItem>
                        <DataValue>{profile.adIndex.toLocaleString()}</DataValue>
                        <DataLabel>광고지수</DataLabel>
                    </ProfileDataItem>
                </ProfileDataColumn>
            </ProfileData>
            <ButtonGroup>
                <SidebarButton
                    isActive={activeButton === 'postAnalysis'}
                    onClick={() => handleButtonClick('postAnalysis')}
                >
                    포스트 분석
                </SidebarButton>
<<<<<<< HEAD

=======
                <SidebarButton
                    isActive={activeButton === 'reelsAnalysis'}
                    onClick={() => handleButtonClick('reelsAnalysis')}
                >
                    릴스 분석
                </SidebarButton>
>>>>>>> b1f3234aaae7ddd92815398128520eb9238875f3
                <SidebarButton
                    isActive={activeButton === 'followerTrend'}
                    onClick={() => handleButtonClick('followerTrend')}
                >
                    팔로워 분석
                </SidebarButton>
                <SidebarButton
                    isActive={activeButton === 'similarFollower'}
                    onClick={() => handleButtonClick('similarFollower')}
                >
                    유사 인플루언서
                </SidebarButton>
            </ButtonGroup>
            <Logo>LOGO</Logo>
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
`;

const Username = styled.p`
    font-family: Inter;
    font-size: 20px;
    font-weight: 600;
    margin-top: 10px;
`;

const Name = styled.p`
    font-size: 18px;
    font-weight: 500;
    margin: 5px 0;
`;

const Category = styled.p`
    font-size: 16px;
    font-weight: 400;
    color: #666;
    margin-bottom: 20px;
`;

const ProfileData = styled.div`
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin: 20px 0;
    padding: 20px;
`;

const ProfileDataColumn = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
`;

const ProfileDataItem = styled.div`
    text-align: center;
    margin-bottom: 10px;
`;

const DataValue = styled.p`
    font-size: 18px;
    font-weight: 600;
`;

const DataLabel = styled.p`
    font-size: 14px;
    font-weight: 400;
    color: #666;
`;

const ButtonGroup = styled.div`
    width: 100%;
    margin-top: 20px;
`;

const SidebarButton = styled.button`
    display: flex;
    height: 55px;
    width: 210px;
    padding: 15px;
    flex-direction: column;
    gap: 10px;
    align-self: stretch;
    margin-bottom: 10px;
    border: none;
    border-radius: 10px;
    color: var(--white-100, #fff);
    font-size: 16px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    background: ${({ isActive }) =>
        isActive ? 'linear-gradient(90deg, rgba(74, 58, 255, 0.80) 0%, rgba(102, 48, 170, 0.80) 100%)' : '#d3d3d3'};
    cursor: pointer;
    transition: background 0.3s ease;

    &:hover {
        background: ${({ isActive }) =>
            isActive
                ? 'linear-gradient(90deg, rgba(74, 58, 255, 0.80) 0%, rgba(102, 48, 170, 0.80) 100%)'
                : 'rgba(200, 200, 200, 1)'};
    }
`;

const Logo = styled.div`
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
    text-transform: uppercase;
`;
