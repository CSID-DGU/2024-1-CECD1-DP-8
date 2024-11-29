import React from 'react';
import styled from 'styled-components';

export default function ReportCard({ profile }) {
    return (
        <CardWrapper>
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
        </CardWrapper>
    );
}
const CardWrapper = styled.div`
    width: 282px;
    padding: 20px;
    border-radius: 20px;
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    height: 600px; /* PC 버전 고정 높이 유지 */

    @media (max-width: 768px) {
        height: auto; /* 모바일에서 자동 높이 */
        min-height: 500px; /* 최소 높이 설정 */
        padding: 16px;
        overflow: hidden;
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
        white-space: nowrap; /* 텍스트를 한 줄로 표시 */
        overflow: hidden; /* 초과 텍스트 숨김 */
        text-overflow: ellipsis; /* ... 처리 */
    }
`;

const Name = styled.p`
    font-size: 18px;
    font-weight: 500;
    margin: 5px 0;

    @media (max-width: 768px) {
        font-size: 16px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
`;

const Category = styled.p`
    font-size: 16px;
    font-weight: 400;
    color: #666;
    margin-bottom: 20px;

    @media (max-width: 768px) {
        font-size: 14px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
`;

const ProfileData = styled.div`
    display: flex;
    justify-content: space-around;
    width: 100%;
    margin: 20px 0;
    padding: 20px;

    @media (max-width: 768px) {
        flex-direction: column; /* 모바일에서 수직 정렬 */
        align-items: center;
        gap: 8px; /* 간격 추가 */
        padding: 12px;
    }
`;

const ProfileDataItem = styled.div`
    text-align: center;
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
