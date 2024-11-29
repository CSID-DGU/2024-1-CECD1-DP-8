import React from 'react';
import { Pie } from 'react-chartjs-2';
import styled from 'styled-components';
import likeIcon from '../../assets/like-icon.png';
import commentIcon from '../../assets/comment-icon.png';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

// ChartJS 요소 등록
ChartJS.register(ArcElement, Tooltip, Legend);

export default function ReportAdditionalStats({
    feedCnt,
    reelsCnt,
    adCnt,
    nonAdCnt,
    commentsAvgOfAdMedia,
    likeAvgOfAdMedia,
}) {
    const totalFeedReels = feedCnt + reelsCnt;
    const totalAdNonAd = adCnt + nonAdCnt;

    const calculatePercentage = (part, total) => ((part / total) * 100).toFixed(1);

    const feedReelsData = {
        labels: [
            `피드 (${calculatePercentage(feedCnt, totalFeedReels)}%)`,
            `릴스 (${calculatePercentage(reelsCnt, totalFeedReels)}%)`,
        ],
        datasets: [
            {
                data: [feedCnt, reelsCnt],
                backgroundColor: ['#4A58FF', '#FF8C42'],
                hoverBackgroundColor: ['#4A58FFCC', '#FF8C42CC'],
            },
        ],
    };

    const adNonAdData = {
        labels: [
            `광고 (${calculatePercentage(adCnt, totalAdNonAd)}%)`,
            `비광고 (${calculatePercentage(nonAdCnt, totalAdNonAd)}%)`,
        ],
        datasets: [
            {
                data: [adCnt, nonAdCnt],
                backgroundColor: ['#FF5252', '#42A5F5'],
                hoverBackgroundColor: ['#FF5252CC', '#42A5F5CC'],
            },
        ],
    };

    const options = {
        plugins: {
            legend: {
                display: true,
                labels: {
                    boxWidth: 20,
                    padding: 15,
                    font: {
                        size: 14,
                    },
                },
            },
        },
    };

    return (
        <Wrapper>
            <ChartsWrapper>
                <ChartBox>
                    <PieChartWrapper>
                        <Pie data={feedReelsData} options={options} />
                    </PieChartWrapper>
                    <ChartLabel>피드·릴스 비율</ChartLabel>
                </ChartBox>
                <ChartBox>
                    <PieChartWrapper>
                        <Pie data={adNonAdData} options={options} />
                    </PieChartWrapper>
                    <ChartLabel>광고 게시글 비율</ChartLabel>
                </ChartBox>
            </ChartsWrapper>
            <StatsWrapper>
                <StatBox>
                    <Label>광고 게시물 평균 좋아요</Label>
                    <StatContent>
                        <img src={likeIcon} alt="좋아요 아이콘" />
                        <DataValue>{likeAvgOfAdMedia.toFixed(1)}</DataValue>
                    </StatContent>
                </StatBox>
                <StatBox>
                    <Label>광고 게시물 평균 댓글</Label>
                    <StatContent>
                        <img src={commentIcon} alt="댓글 아이콘" />
                        <DataValue>{commentsAvgOfAdMedia.toFixed(1)}</DataValue>
                    </StatContent>
                </StatBox>
            </StatsWrapper>
        </Wrapper>
    );
}
const Wrapper = styled.div`
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-top: 20px;
    border-radius: 12px;
`;

const ChartsWrapper = styled.div`
    display: flex;
    justify-content: space-between;
    gap: 20px;

    @media (max-width: 768px) {
        flex-direction: column;
        align-items: center;
    }
`;

const ChartBox = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    padding: 20px;
    border-radius: 16px;
    background-color: #ffffff;

    @media (max-width: 768px) {
        width: 100%;
        max-width: 350px;
    }
`;

const PieChartWrapper = styled.div`
    width: 100%;
    max-width: 280px;
    margin-bottom: 10px;
    height: 250px;
    @media (max-width: 768px) {
        max-width: 240px;
    }
`;

const ChartLabel = styled.p`
    font-size: 18px;
    font-weight: 600;
    color: #333;
    margin-top: 10px;
    text-align: center;
`;

const StatsWrapper = styled.div`
    display: flex;
    justify-content: space-between;
    gap: 20px;

    @media (max-width: 768px) {
        flex-direction: column;
        align-items: center;
    }
`;

const StatBox = styled.div`
    flex: 1;
    padding: 20px;
    border-radius: 16px;
    background-color: #ffffff;
    text-align: center;

    @media (max-width: 768px) {
        width: 100%;
        max-width: 350px;
    }
`;

const Label = styled.h3`
    font-size: 16px;
    font-weight: 600;
    color: #333;
    margin-bottom: 10px;
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

const DataValue = styled.span`
    font-size: 24px;
    font-weight: 700;
    color: #4a3aff;
`;
