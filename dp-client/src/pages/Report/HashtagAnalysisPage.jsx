import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip } from 'chart.js';
import { fetchData } from '../../services/api';
import Spinner from '../../components/Spinner/Spinner';
ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip);

export default function PostAnalysisPage({ id }) {
    const [usageCounts, setUsageCounts] = useState([]);
    const [avgEngagements, setAvgEngagements] = useState([]);
    const [maxEngagements, setMaxEngagements] = useState([]);
    const [totalEngagements, setTotalEngagements] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchHashTagData = async () => {
            try {
                setLoading(true);
                const response = await fetchData(`/influencer/report/hash-tags/${id}`);
                const { usageCounts, avgEngagements, maxEngagements, totalEngagements } = response.result;

                // 데이터 저장 (내림차순 정렬)
                setUsageCounts([...usageCounts].sort((a, b) => b.usageCount - a.usageCount));
                setAvgEngagements([...avgEngagements].sort((a, b) => b.avgEngagement - a.avgEngagement));
                setMaxEngagements([...maxEngagements].sort((a, b) => b.maxEngagement - a.maxEngagement));
                setTotalEngagements([...totalEngagements].sort((a, b) => b.totalEngagement - a.totalEngagement));
            } catch (err) {
                setError('데이터를 가져오는 중 오류가 발생했습니다.');
            } finally {
                setLoading(false);
            }
        };

        if (id) fetchHashTagData();
    }, [id]);

    if (loading) return <Spinner />;
    if (error) return <ErrorMessage>{error}</ErrorMessage>;

    // 그래프 데이터 생성 함수
    const createBarChartData = (data, labelKey, valueKey) => ({
        labels: data.map((item) => item[labelKey]),
        datasets: [
            {
                label: valueKey,
                data: data.map((item) => item[valueKey]),
                backgroundColor: 'rgba(74, 58, 255, 0.8)',
                borderColor: 'rgba(74, 58, 255, 1)',
                borderWidth: 1,
            },
        ],
    });

    return (
        <AnalysisWrapper>
            <Notice>*참여율 = 좋아요 + 댓글 수 입니다.</Notice>
            <GraphBox>
                <GraphTitle>해시태그 사용 빈도</GraphTitle>
                <Bar
                    data={createBarChartData(usageCounts, 'hashTag', 'usageCount')}
                    options={{
                        responsive: true,
                        plugins: {
                            legend: { display: false },
                        },
                        scales: {
                            x: { grid: { display: false }, ticks: { font: { size: 12 } } },
                            y: { grid: { color: 'rgba(200, 200, 200, 0.3)' }, ticks: { font: { size: 12 } } },
                        },
                    }}
                />
            </GraphBox>
            <GraphBox>
                <GraphTitle>평균 해시태그 참여율</GraphTitle>
                <Bar
                    data={createBarChartData(avgEngagements, 'hashTag', 'avgEngagement')}
                    options={{
                        responsive: true,
                        plugins: {
                            legend: { display: false },
                        },
                        scales: {
                            x: { grid: { display: false }, ticks: { font: { size: 12 } } },
                            y: { grid: { color: 'rgba(200, 200, 200, 0.3)' }, ticks: { font: { size: 12 } } },
                        },
                    }}
                />
            </GraphBox>
            <GraphBox>
                <GraphTitle>최대 해시태그 참여율</GraphTitle>
                <Bar
                    data={createBarChartData(maxEngagements, 'hashTag', 'maxEngagement')}
                    options={{
                        responsive: true,
                        plugins: {
                            legend: { display: false },
                        },
                        scales: {
                            x: { grid: { display: false }, ticks: { font: { size: 12 } } },
                            y: { grid: { color: 'rgba(200, 200, 200, 0.3)' }, ticks: { font: { size: 12 } } },
                        },
                    }}
                />
            </GraphBox>
            <GraphBox>
                <GraphTitle>총 해시태그 참여율</GraphTitle>
                <Bar
                    data={createBarChartData(totalEngagements, 'hashTag', 'totalEngagement')}
                    options={{
                        responsive: true,
                        plugins: {
                            legend: { display: false },
                        },
                        scales: {
                            x: { grid: { display: false }, ticks: { font: { size: 12 } } },
                            y: { grid: { color: 'rgba(200, 200, 200, 0.3)' }, ticks: { font: { size: 12 } } },
                        },
                    }}
                />
            </GraphBox>
        </AnalysisWrapper>
    );
}

const AnalysisWrapper = styled.div`
    display: flex;
    flex-direction: column;
    gap: 30px;
    padding: 20px;
    max-width: 900px;
    margin: 0 auto;

    @media (max-width: 768px) {
        padding: 15px;
        gap: 20px;
    }
`;

const Notice = styled.p`
    font-size: 14px;
    color: #666;
    text-align: center;
    margin-bottom: 20px;

    @media (max-width: 768px) {
        font-size: 12px;
    }
`;

const GraphBox = styled.div`
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;

    @media (max-width: 768px) {
        padding: 15px;
    }
`;

const GraphTitle = styled.h3`
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 15px;
    text-align: center;
    color: rgba(74, 58, 255, 0.9);

    @media (max-width: 768px) {
        font-size: 16px;
        margin-bottom: 10px;
    }
`;

const LoadingMessage = styled.div`
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-top: 50px;
`;

const ErrorMessage = styled.div`
    text-align: center;
    font-size: 18px;
    color: black;
    margin-top: 50px;
`;
