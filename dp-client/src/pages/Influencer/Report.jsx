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
    TimeScale,
} from 'chart.js';
import 'chartjs-adapter-date-fns';
import WordCloud from 'react-d3-cloud';
import InfluencerNavbar from '../../components/Navbar/InfluencerNavbar';
import styled, { createGlobalStyle } from 'styled-components';
import data from './data.json';
import likeIcon from '../../assets/like-icon.png';
import commentIcon from '../../assets/comment-icon.png';
import feedimg from '../../assets/feedimg.png';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend, CategoryScale, TimeScale);

export default function Report() {
    const profileData = data.profile;
    const detailData = data.detail;

    const followerTrendData = {
        labels: detailData.followerTrend.map((entry) => entry.timestamp.split('T')[0]),
        datasets: [
            {
                label: '팔로워 추이',
                data: detailData.followerTrend.map((entry) => entry.count),
                fill: false,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
            },
        ],
    };

    const wordCloudData = detailData.hashtag.map((word) => ({ text: word, value: 1000 }));

    return (
        <>
            <GlobalStyle/>
            <InfluencerNavbar />

            <Wrapper>
                <LeftSection>
                    <Intro>
                        <ProfileImage>
                            <img src={profileData.profileImage} alt="프로필" />
                        </ProfileImage>
                        <Username>@{profileData.instaName}</Username>
                        <Name>{profileData.userName}</Name>
                        <Category>{data.category}</Category>
                        <ProfileData>
                            <ProfileDataColumn>
                                <ProfileDataItem>
                                    <DataValue>{data.mediaCnt.toLocaleString()}</DataValue>
                                    <DataLabel>게시글</DataLabel>
                                </ProfileDataItem>
                                <ProfileDataItem>
                                    <DataValue>{data.follwerCnt.toLocaleString()}</DataValue>
                                    <DataLabel>팔로워</DataLabel>
                                </ProfileDataItem>
                            </ProfileDataColumn>
                            <ProfileDataColumn>
                                <ProfileDataItem>
                                    <DataValue>{data.InfluenceIndex.toLocaleString()}</DataValue>
                                    <DataLabel>영향력지수</DataLabel>
                                </ProfileDataItem>
                                <ProfileDataItem>
                                    <DataValue>{data.adIndex.toLocaleString()}</DataValue>
                                    <DataLabel>광고지수</DataLabel>
                                </ProfileDataItem>
                            </ProfileDataColumn>
                        </ProfileData>
                    </Intro>
                </LeftSection>
                <DataSection>
                    <SectionTitle>인기 포스트</SectionTitle>
                    <PostSection>
                        {data.media.map((post) => (
                            <Post key={post.mediaId}>
                                <PostImage src={post.imageUrl} alt="게시글" />
                                <PostStats>
                                    <span>❤️ {post.likeCnt}</span>
                                    <span>💬 {post.commentCnt}</span>
                                </PostStats>
                            </Post>
                        ))}
                    </PostSection>
                    <SectionTitle>상세 분석</SectionTitle>
                    <FollowerSection>
                        <FollowerTrend>
                            <Line
                                data={followerTrendData}
                                options={{
                                    scales: {
                                        x: {
                                            type: 'time',
                                            time: {
                                                unit: 'day',
                                            },
                                        },
                                        y: {
                                            beginAtZero: true,
                                        },
                                    },
                                }}
                            />
                        </FollowerTrend>
                        <ReactionIndex>반응지수 {detailData.reactionCnt}</ReactionIndex>
                    </FollowerSection>
                    <HashtagSection>
                        <PostHashtag>
                            <WordCloud
                                data={wordCloudData}
                                fontSizeMapper={(word) => Math.log2(word.value) * 5}
                                rotate={() => 0}
                            />
                        </PostHashtag>
                        <ResponsiveHashtag>{detailData.popularity_hashtag}</ResponsiveHashtag>
                    </HashtagSection>
                    <AverageSection>
                        <Like>
                            <img src={likeIcon} alt="좋아요 아이콘" />
                            <DataValue>{detailData.likeAvg}</DataValue>
                            <DataLabel>평균 좋아요</DataLabel>
                        </Like>
                        <Comment>
                            <img src={commentIcon} alt="댓글 아이콘" />
                            <DataValue>{detailData.commentAvg}</DataValue>
                            <DataLabel>평균 댓글수</DataLabel>
                        </Comment>
                        <Upload>
                            <DataValue>{detailData.uploadCycle}</DataValue>
                            <DataLabel>게시물 업로드 주기</DataLabel>
                        </Upload>
                    </AverageSection>
                    <SummarySection>
                        <Summary>
                            {data.category} 게시물을 이번달 {detailData.activitySummary}개 올렸어요!
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
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: row;
    background-color: var(--background--gray);
`;

const Intro = styled.div`
    width: 80%;
    height: 570px;
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

const DataValue = styled.p`
    font-family: Inter;
    font-size: 18px;
    font-weight: 600;
`;

const DataLabel = styled.p`
    font-family: Inter;
    font-size: 14px;
    font-weight: 400;
    color: #666;
`;

const Logo = styled.div`
    font-family: Inter;
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
`;

const LeftSection = styled.div`
    width: var(--report-left);
`

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
    padding: 20px 20px 11px 20px;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
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
    width: 100%;
    height: 570px;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
`;

const FollowerTrend = styled.div`
    display: flex;
    width: 70%;
    height: 500px;
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
    width: 20%;
    height: 500px;
    flex-shrink: 0;
    border-radius: 20px;
    margin-left: 30px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    justify-content: center;
    align-items: center;
    font-family: Inter;
    font-size: 25px;
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
    flex-direction: row;
`;

const PostHashtag = styled.div`
    display: flex;
    width: 60%;
    height: 500px;
    flex-shrink: 0;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    justify-content: center;
    align-items: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    padding: 5px;
`;

const ResponsiveHashtag = styled.div`
    display: flex;
    width: 20%;
    height: 500px;
    flex-shrink: 0;
    border-radius: 20px;
    margin-left: 95px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    justify-content: center;
    align-items: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    padding: 5px;
`;

const AverageSection = styled.div`
    width: 100%;
    height: 380px;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
`;

const Like = styled.div`
    width: calc(var(--report-right) / 3);
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
    width: calc(var(--report-right) / 3);
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
    width: calc(var(--report-right) / 3);
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
    width: 100%;
    height: 550px;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
`;

const Summary = styled.div`
    display: flex;
    width: 850px;
    height: 400px;
    flex-shrink: 0;
    border-radius: 20px;
    background: #fff;
    box-shadow: 0px 3px 100px 0px rgba(0, 0, 0, 0.1);
    color: #000;
    text-align: center;
    justify-content: center;
    align-items: center;
    font-family: Inter;
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    padding: 20px;
`;
