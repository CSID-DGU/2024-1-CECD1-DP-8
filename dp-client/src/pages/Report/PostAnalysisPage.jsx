import React, { useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';
import styled from 'styled-components';
import likeIcon from '../../assets/like-icon.png';
import commentIcon from '../../assets/comment-icon.png';
import WordCloudComponent from '../../components/Report/WordCloudComponent'; // New Component

// Register chart.js components
ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function PostAnalysisPage({ reportData }) {
    const [period, setPeriod] = useState('W'); // Default period is 'Weekly'

    const {
        mostThreePosts = [],
        allTagsOfMedias = [],
        reactionQuotient = [0],
        currentWeekLikeAvg = 0,
        currentWeekCommentsAvg = 0,
        adMediaRatio = 0,
        reelsRatio = 0,
        reelsChartLikes = [],
        reelsChartComments = [],
        likeAvg = 0,
        commentsAvg = 0,
    } = reportData || {}; // Fallback to default values if properties are missing

    const handlePeriodChange = (newPeriod) => {
        setPeriod(newPeriod); // Update the period
        // Fetch updated data if needed
    };

    // Instagram 임베드 함수
    const renderInstagramEmbed = () => {
        const postUrl = `https://www.instagram.com/p/DAh-22YTWWf/embed`; // 고유코드 사용
        return (
            <iframe
                src={postUrl}
                width="400"
                height="480"
                frameBorder="0"
                scrolling="no"
                allowTransparency="true"
                allow="encrypted-media"
                title="Instagram Post"
            ></iframe>
        );
    };

    // Handle -1 cases and round values
    const renderValue = (value) => (value === -1 ? '숨김' : Math.round(value));

    // Prepare data for the charts
    const likesData = {
        labels: reelsChartLikes.map((item) => item.postedAt),
        datasets: [
            {
                label: 'Reels Likes Trend',
                data: reelsChartLikes.map((item) => item.totalCnt),
                fill: false,
                backgroundColor: '#4A3AFF',
                borderColor: '#4A3AFF',
            },
        ],
    };

    const commentsData = {
        labels: reelsChartComments.map((item) => item.postedAt),
        datasets: [
            {
                label: 'Reels Comments Trend',
                data: reelsChartComments.map((item) => item.totalCnt),
                fill: false,
                backgroundColor: '#FF3A4A',
                borderColor: '#FF3A4A',
            },
        ],
    };

    // Word Cloud data mapping
    const wordCloudData = allTagsOfMedias.map((tag) => ({
        text: tag,
        value: Math.random() * 1000 + 100, // Random value to simulate tag size
    }));

    return (
        <PostAnalysisWrapper>
            {/* Period Selector */}
            <PeriodSelector>
                <PeriodButton active={period === 'W'} onClick={() => handlePeriodChange('W')}>
                    주간 리포트
                </PeriodButton>
                <PeriodButton active={period === 'D'} onClick={() => handlePeriodChange('D')}>
                    일간 리포트
                </PeriodButton>
            </PeriodSelector>

            {/* 인기 포스트 Section */}
            <Section>
                <SectionTitle>인기 포스트</SectionTitle>
                <PostSection>
                    {/* 모든 포스트에 동일한 고유코드 적용 */}
                    {mostThreePosts.map((_, index) => (
                        <Post key={index}>
                            {renderInstagramEmbed()} {/* Instagram 임베드 */}
                        </Post>
                    ))}
                </PostSection>
            </Section>

            {/* Analysis Section */}
            <Section>
                <AnalysisWrapper>
                    <WordCloudSection>
                        <Label>게시글 해시태그</Label>
                        <WordCloudComponent wordCloudData={wordCloudData} />
                    </WordCloudSection>
                    <ReactionIndexSection>
                        <Label>반응지수</Label>
                        <Reaction>
                            <ReactionData>{renderValue(reactionQuotient[0])}% EGR</ReactionData>
                            <Description>동일 팔로워군 비교 그래프</Description>
                        </Reaction>
                    </ReactionIndexSection>
                </AnalysisWrapper>
            </Section>

            <Section>
                <AverageStatsWrapper>
                    <StatBox>
                        <Label>전체 게시글의 평균 좋아요</Label>
                        <StatContent>
                            <img src={likeIcon} alt="좋아요 아이콘" />
                            <DataValue>{renderValue(likeAvg)}</DataValue>
                        </StatContent>
                    </StatBox>
                    <StatBox>
                        <Label>전체 게시글의 평균 댓글</Label>
                        <StatContent>
                            <img src={commentIcon} alt="댓글 아이콘" />
                            <DataValue>{renderValue(commentsAvg)}</DataValue>
                        </StatContent>
                    </StatBox>
                    <StatBox>
                        <Label>최근 게시글의 평균 좋아요</Label>
                        <StatContent>
                            <img src={likeIcon} alt="좋아요 아이콘" />
                            <DataValue>{renderValue(currentWeekLikeAvg)}</DataValue>
                        </StatContent>
                    </StatBox>
                    <StatBox>
                        <Label>최근 게시글의 평균 댓글</Label>
                        <StatContent>
                            <img src={commentIcon} alt="댓글 아이콘" />
                            <DataValue>{renderValue(currentWeekCommentsAvg)}</DataValue>
                        </StatContent>
                    </StatBox>
                </AverageStatsWrapper>
            </Section>
            <Section>
                <GraphWrapper>
                    <GraphBox>
                        <Label>릴스 좋아요 추이</Label>
                        <Line data={likesData} />
                    </GraphBox>
                    <GraphBox>
                        <Label>릴스 댓글 추이</Label>
                        <Line data={commentsData} />
                    </GraphBox>
                </GraphWrapper>
            </Section>
        </PostAnalysisWrapper>
    );
}

// Styled components for layout
const PostAnalysisWrapper = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    min-width: 1000px;
    padding: 40px;
    box-sizing: border-box;
`;

const PeriodSelector = styled.div`
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
`;

const PeriodButton = styled.button`
    background-color: ${(props) => (props.active ? '#4A3AFF' : '#ddd')};
    color: white;
    border: none;
    padding: 10px 20px;
    margin-left: 10px;
    border-radius: 5px;
    cursor: pointer;
`;
const Section = styled.div`
    margin-bottom: 30px;
`;

const SectionTitle = styled.h2`
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 20px;
`;

const PostSection = styled.div`
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
`;

const Post = styled.div`
    border-radius: 20px;
    background-color: #fff;
    padding: 10px;
    text-align: center;
    min-height: 200px;
`;

const PostImage = styled.img`
    width: 100%;
    height: auto;
    border-radius: 15px;
`;

const PostStats = styled.div`
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
`;

const StatItem = styled.div`
    display: flex;
    align-items: center;

    img {
        width: 20px;
        height: 20px;
        margin-right: 5px;
    }
`;

const StatText = styled.span`
    font-size: 16px;
`;

const Description = styled.p`
    color: #000;
    text-align: center;
    font-size: 19px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;
const AnalysisWrapper = styled.div`
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
`;

const WordCloudSection = styled.div`
    padding: 20px;
    border-radius: 20px;
    background-color: #fff;
`;

const ReactionIndexSection = styled.div`
    padding: 20px;
    border-radius: 20px;
    background-color: #fff;
    text-align: center;
    justify-content: center;
`;

const Label = styled.h3`
    color: #000;
    text-align: center;
    font-size: 19px;
    font-weight: 600;
    line-height: normal;
    margin-bottom: 10px;
`;

const Reaction = styled.div`
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 160px;
`;

const ReactionData = styled.p`
    font-size: 24px;
    font-weight: 600;
    color: #7f00ff;
`;

const AverageStatsWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* Four columns for the stats */
    gap: 20px;
    margin-top: 30px;
`;

const StatBox = styled.div`
    padding: 20px;
    border-radius: 20px;
    background-color: #fff;
    text-align: center;
`;

const StatContent = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;

    img {
        width: 40px;
        height: 40px;
        margin-right: 10px;
    }
`;

const DataValue = styled.p`
    color: #4a3aff;
    font-size: 32px;
    font-weight: 600;
`;

const GraphWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 30px;
`;

const GraphBox = styled.div`
    padding: 20px;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border-radius: 20px;
    text-align: center;
    align-items: center;
`;

const Circle = styled.div`
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: linear-gradient(90deg, rgba(74, 58, 255, 0.8) 0%, rgba(102, 48, 170, 0.8) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
`;

const CircleText = styled.p`
    font-size: 24px;
    font-weight: 500;
    color: #fff;
`;
