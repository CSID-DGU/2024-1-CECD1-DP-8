import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, CategoryScale, LinearScale, PointElement, TimeScale } from 'chart.js';
import styled from 'styled-components';
import likeIcon from '../../assets/like-icon.png';
import commentIcon from '../../assets/comment-icon.png';
import WordCloudComponent from '../../components/Report/WordCloudComponent'; // New Component
import 'chartjs-adapter-date-fns';
// Register chart.js components
ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, TimeScale);

export default function PostAnalysisPage({ reportData }) {
    const [period, setPeriod] = useState('W'); // Default period is 'Weekly'
    const [isLoadingWordCloud, setIsLoadingWordCloud] = useState(true); // WordCloudComponent 로딩 상태

    const {
        mostThreePostsCodes = [],
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
        followerCharts = [], // 팔로워 추이 데이터
    } = reportData || {}; // Fallback to default values if properties are missing

    const handlePeriodChange = (newPeriod) => {
        setPeriod(newPeriod); // Update the period
    };

    const renderInstagramEmbed = (uniqueCode) => {
        try {
            const postUrl = `https://www.instagram.com/p/${uniqueCode}/embed`; // 고유코드 사용
            console.log('Embedding Instagram post:', postUrl); // 고유코드 확인용 콘솔 로그
            return (
                <iframe
                    src={postUrl}
                    width="300"
                    height="600"
                    frameBorder="0"
                    scrolling="no"
                    allowTransparency="true"
                    allow="encrypted-media"
                    title="Instagram Post"
                ></iframe>
            );
        } catch (error) {
            console.error('Error embedding Instagram post:', error);
            return <div>Instagram 포스트를 로드하는 데 실패했습니다.</div>;
        }
    };

    // WordCloud 로딩 완료 후 호출
    useEffect(() => {
        setTimeout(() => {
            setIsLoadingWordCloud(false); // 일정 시간 후에 로딩 상태를 false로 변경
        }, 2000); // 2초 후 로딩 완료 시뮬레이션
    }, []);

    // Handle -1 cases and round values
    const renderValue = (value) => (value === -1 ? '숨김' : Math.round(value));

    // Prepare data for the charts
    const likesData = {
        labels: reelsChartLikes.map((item) => item.postedAt),
        datasets: [
            {
                label: '릴스 좋아요 추이',
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
                label: '릴스 댓글 추이',
                data: reelsChartComments.map((item) => item.totalCnt),
                fill: false,
                backgroundColor: '#FF3A4A',
                borderColor: '#FF3A4A',
            },
        ],
    };
    const followerTrendData = {
        labels: followerCharts.map((entry) => entry.createdAt), // x축 데이터 (날짜)
        datasets: [
            {
                label: '팔로워 추이',
                data: followerCharts.map((entry) => entry.followerCnt), // y축 데이터 (팔로워 수)
                borderColor: 'rgba(103, 58, 183, 1)', // 선 색상
                backgroundColor: 'rgba(103, 58, 183, 0.2)', // 투명 배경색
                fill: true, // 배경색 채우기
                tension: 0.4, // 곡선 정도
                pointRadius: 5, // 포인트 크기
                pointBackgroundColor: 'rgba(255, 255, 255, 1)', // 포인트 배경색
                pointBorderColor: 'rgba(103, 58, 183, 1)', // 포인트 테두리 색상
                pointHoverRadius: 8, // 호버 시 포인트 크기
            },
        ],
    };

    const followerTrendOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
                labels: {
                    color: '#333',
                    font: {
                        size: 14,
                        family: "'Roboto', sans-serif",
                    },
                },
            },
            tooltip: {
                enabled: true,
                backgroundColor: 'rgba(50, 50, 50, 0.8)',
                titleColor: '#fff',
                bodyColor: '#fff',
                borderColor: 'rgba(103, 58, 183, 1)',
                borderWidth: 1,
                cornerRadius: 4,
            },
        },
        scales: {
            x: {
                type: 'time', // 시간 데이터로 설정
                time: { unit: 'day', tooltipFormat: 'yyyy-MM-dd' }, // 일 단위 표시
                grid: {
                    color: 'rgba(200, 200, 200, 0.3)',
                    drawBorder: true,
                },
                ticks: {
                    color: '#666',
                    font: {
                        size: 12,
                    },
                },
            },
            y: {
                beginAtZero: true,
                grid: {
                    color: 'rgba(200, 200, 200, 0.3)',
                    drawBorder: true,
                },
                ticks: {
                    stepSize: 10,
                    color: '#666',
                    font: {
                        size: 12,
                    },
                },
            },
        },
        animation: {
            duration: 1500,
            easing: 'easeInOutQuart',
        },
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
                    {mostThreePostsCodes.length === 0 && <p>인기 포스트가 없습니다.</p>}
                    {mostThreePostsCodes.map((post, index) => {
                        return (
                            <Post key={index}>
                                {renderInstagramEmbed(post.uniqueCode)} {/* Instagram 임베드 */}
                            </Post>
                        );
                    })}
                </PostSection>
            </Section>

            {/* Analysis Section */}
            <Section>
                <AnalysisWrapper>
                    <WordCloudSection>
                        <Label>게시글 해시태그</Label>
                        {isLoadingWordCloud ? (
                            <SpinnerWrapper>
                                <Spinner /> {/* 로딩 중일 때 스피너 */}
                            </SpinnerWrapper>
                        ) : (
                            <WordCloudComponent wordCloudData={wordCloudData} /> // WordCloud 렌더링
                        )}
                    </WordCloudSection>
                    <ReactionIndexSection>
                        <Label>반응지수</Label>
                        <Reaction>
                            <ReactionData>{renderValue(reactionQuotient[0])}% EGR</ReactionData>
                            <Description>동일 팔로워군과 비교한 수치에요.</Description>
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
            <Section>
                <Section>
                    <FollowerTrendWrapper>
                        <Label>팔로워 추이</Label>
                        <FollowerChartWrapper>
                            <Line data={followerTrendData} options={followerTrendOptions} />
                        </FollowerChartWrapper>
                    </FollowerTrendWrapper>
                </Section>
            </Section>
        </PostAnalysisWrapper>
    );
}

const PostAnalysisWrapper = styled.div`
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 5%;
`;

const PeriodButton = styled.button`
    background: ${(props) =>
        props.active ? 'linear-gradient(90deg, rgba(74, 58, 255, 0.80) 0%, rgba(102, 48, 170, 0.80) 100%)' : '#ddd'};
    color: white;
    padding: 8px 16px;
    margin-left: 8px;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease;
    font-size: 14px;
`;

const PostSection = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* 최소 크기를 줄임 */
    gap: 16px;
`;

const PeriodSelector = styled.div`
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
`;
const Section = styled.div`
    margin-bottom: 30px;
`;

const SectionTitle = styled.h2`
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 20px;
`;
const Post = styled.div`
    border-radius: 16px;
    background-color: #fff;
    padding: 8px;
    text-align: center;
    min-height: 180px;
`;

const AnalysisWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* 최소 크기 조정 */
    gap: 16px;
    margin-top: 16px;
`;

const WordCloudSection = styled.div`
    padding: 16px;
    border-radius: 16px;
    background-color: #fff;
`;

const ReactionIndexSection = styled.div`
    padding: 16px;
    border-radius: 16px;
    background-color: #fff;
    text-align: center;
    justify-content: center;
`;

const Label = styled.h3`
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    line-height: normal;
    margin-bottom: 8px;
`;

const AverageStatsWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* 최소 크기 감소 */
    gap: 16px;
    margin-top: 24px;
`;

const StatBox = styled.div`
    padding: 16px;
    border-radius: 16px;
    background-color: #fff;
    text-align: center;
`;

const StatContent = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;

    img {
        width: 32px;
        height: 32px;
        margin-right: 8px;
    }
`;

const DataValue = styled.p`
    color: #4a3aff;
    font-size: 24px;
    font-weight: 600;
`;

const GraphWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* 최소 크기 조정 */
    gap: 16px;
    margin-top: 24px;
`;

const GraphBox = styled.div`
    padding: 16px;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border-radius: 16px;
    text-align: center;
    align-items: center;
`;

const FollowerChartWrapper = styled.div`
    height: 300px;
`;

const Reaction = styled.div`
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 100px;
    flex-direction: column;
`;

const ReactionData = styled.p`
    font-size: 50px;
    font-weight: 600;
    color: #7f00ff;
`;

const Description = styled.p`
    color: #000;
    text-align: center;
    font-size: 22px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    margin-top: 20px;
`;
const SpinnerWrapper = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    height: 300px;
`;

const Spinner = styled.div`
    border: 6px solid #f3f3f3;
    border-top: 6px solid #7f00ff;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 1s linear infinite;

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
`;
const FollowerTrendWrapper = styled.div`
    padding: 20px;
    border-radius: 20px;
    background-color: #fff;
    text-align: center;
`;
