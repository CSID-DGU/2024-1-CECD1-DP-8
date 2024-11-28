import React, { useMemo } from 'react';
import styled from 'styled-components';

export default function FollowerTrendIndicator({ followerCharts }) {
    // 최근 한 달의 팔로워 데이터를 필터링
    const recentMonthData = useMemo(() => {
        const now = new Date();
        const oneMonthAgo = new Date();
        oneMonthAgo.setMonth(now.getMonth() - 1);

        return followerCharts.filter((entry) => {
            const createdAt = new Date(entry.createdAt);
            return createdAt >= oneMonthAgo && createdAt <= now;
        });
    }, [followerCharts]);

    // 팔로워 추이 계산
    const trend = useMemo(() => {
        if (!recentMonthData || recentMonthData.length < 2) return '데이터 부족 📊';

        const firstValue = recentMonthData[0].followerCnt;
        const lastValue = recentMonthData[recentMonthData.length - 1].followerCnt;

        const change = lastValue - firstValue;
        const percentageChange = (change / firstValue) * 100;

        if (percentageChange > 2) {
            return '최근 팔로워가 상승세에요! 🚀';
        } else if (percentageChange < -2) {
            return '최근 팔로워가 감소하고있어요. 📉';
        } else {
            return '팔로워가 안정적으로 유지되고있어요. 🌟';
        }
    }, [recentMonthData]);

    return (
        <TrendWrapper>
            <TrendValue>{trend}</TrendValue>
        </TrendWrapper>
    );
}

const TrendWrapper = styled.div`
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    margin-top: 20px;

    @media (max-width: 768px) {
        padding: 16px;
    }
`;

const TrendValue = styled.p`
    font-family: 'Inter', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #7f00ff;
    line-height: 1.5;

    @media (max-width: 768px) {
        font-size: 22px;
    }
`;
