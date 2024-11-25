import React, { useState } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';

export default function ProfileCard({ profile }) {
    const navigate = useNavigate();
    const [showTags, setShowTags] = useState(false);

    const handleHover = () => {
        setShowTags(true);
    };

    const handleLeave = () => {
        console.log('Profile Data:', profile); // 전체 데이터 확인
        console.log('allTagsOfMedias:', profile.result?.allTagsOfMedias); // 해시태그 확인
        setShowTags(false);
    };

    // Check if allTagsOfMedias exists and slice top 3 tags safely
    const topTags =
        Array.isArray(profile.allTagsOfMedias) && profile.allTagsOfMedias.length > 0
            ? profile.allTagsOfMedias.slice(0, 3)
            : [];

    return (
        <CardWrapper>
            <ProfileImage>
                <img src={profile.profilePictureUrl} alt="프로필" />
            </ProfileImage>
            <ProfileDetails>
                <TopRow>
                    <Username>@{profile.nickname}</Username>
                    <CategorySection>
                        <CategoryTitle>카테고리</CategoryTitle>
                        <Category>{profile.category}</Category>
                    </CategorySection>
                </TopRow>
                <Name>{profile.name}</Name>
                <BottomRow>
                    <ProfileDataItem>
                        <DataValue>{profile.followerCnt.toLocaleString()}</DataValue>
                        <DataLabel>팔로워</DataLabel>
                    </ProfileDataItem>
                    <ProfileDataItem>
                        <DataValue>{profile.mediaCnt.toLocaleString()}</DataValue>
                        <DataLabel>게시글</DataLabel>
                    </ProfileDataItem>
                    <ActionButtons>
                        <Button onMouseEnter={handleHover} onMouseLeave={handleLeave}>
                            게시글 해시태그
                        </Button>
                        {showTags && topTags.length > 0 && (
                            <TagsBubble>
                                {topTags.map((tag, index) => (
                                    <Tag key={index}>#{tag}</Tag>
                                ))}
                            </TagsBubble>
                        )}
                        <Button onClick={() => navigate(`/report/${profile.nickname}`)}>리포트 보러가기</Button>
                    </ActionButtons>
                </BottomRow>
            </ProfileDetails>
        </CardWrapper>
    );
}

const CardWrapper = styled.div`
    display: flex;
    align-items: center;
    background: #fff;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    width: 100%;
    position: relative;
`;

const ProfileImage = styled.div`
    width: 80px;
    height: 80px;
    border-radius: 50%;
    overflow: hidden;
    margin-right: 20px;

    img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
`;

const ProfileDetails = styled.div`
    flex: 1;
    display: flex;
    flex-direction: column;
`;

const TopRow = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
`;

const Username = styled.p`
    font-size: 18px;
    font-weight: 600;
    color: #333;
`;

const CategorySection = styled.div`
    text-align: center;
`;

const CategoryTitle = styled.p`
    font-size: 12px;
    font-weight: 500;
    color: #888;
    margin-bottom: 2px;
`;

const Category = styled.span`
    font-size: 14px;
    font-weight: 500;
    color: #fff;
    background: #ff8585;
    padding: 5px 10px;
    border-radius: 15px;
`;

const Name = styled.p`
    font-size: 16px;
    font-weight: 500;
    color: #555;
    margin-bottom: 10px;
`;

const BottomRow = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
`;

const ProfileDataItem = styled.div`
    text-align: left;
`;

const DataValue = styled.p`
    font-size: 18px;
    font-weight: 600;
    color: #333;
`;

const DataLabel = styled.p`
    font-size: 14px;
    font-weight: 400;
    color: #888;
`;

const ActionButtons = styled.div`
    display: flex;
    gap: 10px;
`;

const Button = styled.button`
    font-size: 14px;
    font-weight: 500;
    color: #fff;
    background: #b785ff;
    padding: 10px 15px;
    border: none;
    border-radius: 15px;
    cursor: pointer;

    &:hover {
        background: #9f66ff;
    }
`;

const TagsBubble = styled.div`
    position: absolute;
    top: 60px;
    left: 50%;
    transform: translateX(-50%);
    background: #f7f7f7;
    padding: 10px 15px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    gap: 8px;
`;

const Tag = styled.span`
    font-size: 12px;
    font-weight: 500;
    color: #555;
    background: #e0e0e0;
    padding: 5px 10px;
    border-radius: 10px;
`;
