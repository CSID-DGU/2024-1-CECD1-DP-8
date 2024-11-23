import React, { useState } from 'react';
import styled from 'styled-components';

export default function ProfileCard({ profile, onSelect }) {
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
    justify-content: space-around;
    width: 100%;
    margin: 20px 0;
    padding: 20px;
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
