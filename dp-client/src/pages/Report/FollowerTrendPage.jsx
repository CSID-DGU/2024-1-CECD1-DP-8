import React from 'react';
import { Line } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    LineElement,
    PointElement,
    LinearScale,
    Title,
    Tooltip,
    Legend,
    CategoryScale,
    TimeScale, // 시간 축 등록은 그대로 유지
} from 'chart.js';
import WordCloud from 'react-d3-cloud';
import styled, { createGlobalStyle } from 'styled-components';
import data from './data.json';
import likeIcon from '../../assets/like-icon.png';
import commentIcon from '../../assets/comment-icon.png';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend, CategoryScale, TimeScale);

export default function FollowerTrendPage() {
    const profileData = data.result.profile;
    const mediaList = data.result.mediaList.reportMedias;
    const followerTrend = data.result.followerTrend;
    const tagList = data.result.tagList.tags;
    const highResponseTag = data.result.highResponseTag[0];
    const detailData = data.result;

    const followerTrendData = {
        labels: followerTrend.map((entry) => entry.timestamp.split('T')[0]), // 날짜 문자열 처리
        datasets: [
            {
                label: '팔로워 추이',
                data: followerTrend.map((entry) => entry.count),
                fill: false,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
            },
        ],
    };

    const wordCloudData = tagList.map((word) => ({ text: word.name, value: 1000 }));

    return (
        <>
            <Wrapper>
                <DataSection>
                    <SectionTitle>인기 포스트</SectionTitle>
                    <PostSection>
                        {mediaList.map((post) => (
                            <Post key={post.mediaId}>
                                <PostImage src={post.imageURL} alt="게시글" />
                                <PostStats>
                                    <span>🤍 {post.likeCnt}</span>
                                    <span>💬 {post.replyCnt}</span>
                                </PostStats>
                            </Post>
                        ))}
                    </PostSection>
                    <SectionTitle>상세 분석</SectionTitle>
                    <FollowerSection>
                        <FollowerTrend>
                            <Label>팔로워 추이</Label>
                            <Line
                                data={followerTrendData}
                                options={{
                                    scales: {
                                        x: {
                                            type: 'category', // 시간 축 대신 카테고리 축 사용
                                        },
                                        y: {
                                            beginAtZero: true,
                                        },
                                    },
                                }}
                            />
                        </FollowerTrend>
                        <ReactionIndex>
                            <Label>반응 지수</Label>
                            <ReactionData>{detailData.reactionCnt}</ReactionData>
                            <ReactionDescription>평균보다 높아요!</ReactionDescription>
                        </ReactionIndex>
                    </FollowerSection>

                    <HashtagSection>
                        <PostHashtag>
                            <Label>게시글 해시태그</Label>
                            <WordCloud
                                data={wordCloudData}
                                fontSizeMapper={(word) => Math.log2(word.value) * 5}
                                rotate={() => 0}
                            />
                        </PostHashtag>

                        <ResponsiveHashtag>
                            <Label>반응 높은 해시태그</Label>
                            <HashtagData>{highResponseTag}</HashtagData>
                        </ResponsiveHashtag>
                    </HashtagSection>

                    <AverageSection>
                        <Like>
                            <Label>평균 좋아요</Label>
                            <img src={likeIcon} alt="좋아요 아이콘" />
                            <DataValue>{detailData.likeAvg}</DataValue>
                        </Like>
                        <Comment>
                            <Label>평균 댓글 수</Label>
                            <img src={commentIcon} alt="댓글 아이콘" />
                            <DataValue>{detailData.replyAvg}</DataValue>
                        </Comment>
                        <Upload>
                            <Label>게시물 업로드 주기</Label>
                            <DataValue>{detailData.mediaUploadCycle}</DataValue>
                        </Upload>
                    </AverageSection>

                    <SummarySection>
                        <Summary>
                            <Label>활동 요약</Label>
                            {profileData.category} 게시물을 이번달 {detailData.summary.count}개 올렸어요!
                        </Summary>
                    </SummarySection>
                </DataSection>
            </Wrapper>
        </>
    );
}

// 전역 스타일
const GlobalStyle = createGlobalStyle`
  :root {
    --report-left: 25%;
    --report-right: calc(100% - var(--report-left));
    
  }
`;

const Wrapper = styled.div`
    display: flex;
    flex-direction: row;
    min-width: 1400px;
    white-space: nowrap;
    border-bottom: 0.7px solid #dbe0de;
    position: relative;
    background-color: var(--background--gray);
`;

const Intro = styled.div`
    width: 375px;
    height: 570px;
    flex-shrink: 0;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 33px;
    background: var(--white-100, #fff);
    margin: 50px;
    margin-top: 150px;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    color: #000;
    text-align: center;
    font-family: 'Didact Gothic';
    font-size: 25px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
`;

const ProfileImage = styled.div`
    width: 130px;
    height: 130px;
    margin-top: 36px;
    position: relative;
    border-radius: 50%;
    background: linear-gradient(45deg, #ffdc80, #fcb045, #fd1d1d, #833ab4, #5851db);
    display: flex;
    align-items: center;
    justify-content: center;

    &::before {
        content: '';
        position: absolute;
        top: -5px;
        left: -5px;
        right: -5px;
        bottom: -5px;
        border-radius: 50%;
        background: linear-gradient(45deg, #ffdc80, #fcb045, #fd1d1d, #833ab4, #5851db);
        z-index: -1;
    }

    img {
        width: 90%;
        height: 90%;
        border-radius: 50%;
        border: 2px solid white;
        z-index: 1;
    }
`;

const Username = styled.p`
    font-family: Inter;
    font-size: 20px;
    font-weight: 600;
    margin-top: 20px;
`;

const Name = styled.p`
    font-family: Inter;
    font-size: 18px;
    font-weight: 500;
    margin: 10px 0;
`;

const Category = styled.p`
    font-family: Inter;
    font-size: 16px;
    font-weight: 400;
    color: #666;
    margin-top: 10px;
`;

const ProfileData = styled.div`
    display: flex;
    justify-content: space-around;
    width: 100%;
    margin: 20px 0;
    margin-top: 4rem;
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
const Label = styled.div`
    color: #000;
    text-align: center;
    margin-top: 20px;
    /* Button/Md */
    font-family: Inter;
    font-size: 24px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const DataValue = styled.p`
    font-family: Inter;
    font-size: 18px;
    font-weight: 600;
`;

const DataLabel = styled.p`
    color: #000;
    text-align: center;
    font-feature-settings: 'liga' off, 'clig' off;
    font-family: Abel;
    font-size: 14px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
`;

const Logo = styled.div`
    font-family: Inter;
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
`;

const LeftSection = styled.div`
    width: var(--report-left);
`;

const DataSection = styled.div`
    /*width: 1500px;*/

    width: var(--report-right);
    display: flex;
    flex-direction: column;
    height: auto;
`;

const SectionTitle = styled.p`
    margin: 27px;
    color: #000;
    font-family: Inter;
    font-size: 30px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const PostSection = styled.div`
    width: 100%;
    height: auto;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
`;

const Post = styled.div`
    width: 350px;
    height: 350px;
    flex-shrink: 0;
    margin-top: 10px;
    margin-right: 30px;
    display: inline-flex;

    padding: 20px 20px 20px 20px;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    border-radius: var(--20, 20px);
    background: var(--white-100, #fff);
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
`;

const PostImage = styled.img`
    width: 320px;
    height: 320px;
    border-radius: 20px;
`;

const PostStats = styled.div`
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 0 10px;
    font-size: 18px;
    color: #666;
`;

const FollowerSection = styled.div`
    width: 1280px;
    height: 500px;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    margin-bottom: 30px;
`;

const FollowerTrend = styled.div`
    display: flex;
    padding: 10px;
    flex-direction: column;
    width: 750px;
    height: 450px;
    flex-shrink: 0;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    justify-content: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const ReactionIndex = styled.div`
    display: flex;
    flex-direction: column;
    padding: 10px;
    width: 306px;
    height: 450px;
    flex-shrink: 0;
    border-radius: 20px;
    margin-left: 70px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    align-items: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const ReactionData = styled.div`
    display: flex;
    margin-top: 130px;
    color: #a338f6;
    text-align: center;
    font-family: Inter;
    font-size: 48px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const ReactionDescription = styled.div`
    margin-top: 100px;
    color: #a0a0a0;
    text-align: center;
    font-family: Inter;
    font-size: 20px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const HashtagSection = styled.div`
    width: 100%;
    height: 550px;
    flex-shrink: 0;
    display: flex;
`;

const PostHashtag = styled.div`
    display: flex;
    width: 760px;
    height: 400px;
    padding: 10px;

    flex-shrink: 0;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    justify-content: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const ResponsiveHashtag = styled.div`
    display: flex;
    padding: 10px;
    flex-direction: column;
    width: 300px;
    height: 400px;
    flex-shrink: 0;
    border-radius: 20px;
    margin-left: 85px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;
const HashtagData = styled.div`
    color: #a338f6;
    text-align: center;
    font-family: Inter;
    font-size: 32px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    margin-top: 100px;
`;

const AverageSection = styled.div`
    width: 100%;
    height: 380px;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
`;

const Like = styled.div`
    width: 300px;
    height: 300px;
    flex-shrink: 0;
    margin-top: 10px;
    margin-right: 70px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    text-align: center;
    align-items: center;
    padding: 20px;

    img {
        width: 40px;
        height: 40px;
    }
`;

const Comment = styled.div`
    width: 300px;
    height: 300px;
    flex-shrink: 0;
    margin-top: 10px;
    margin-right: 70px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    text-align: center;
    align-items: center;
    padding: 20px;

    img {
        width: 40px;
        height: 40px;
    }
`;

const Upload = styled.div`
    width: 300px;
    height: 300px;
    flex-shrink: 0;
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    text-align: center;
    align-items: center;
    padding: 20px;
`;

const SummarySection = styled.div`
    width: 1000px;
    height: 500px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    border: 1px solid black;
`;

const Summary = styled.div`
    display: flex;
    flex-direction: column;
    width: 850px;
    height: 400px;
    flex-shrink: 0;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    padding: 20px;
`;
