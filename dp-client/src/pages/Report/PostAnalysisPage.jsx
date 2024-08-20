import React from 'react';
import styled from 'styled-components';
import data from './data.json';
import likeIcon from '../../assets/like-icon.png';
import commentIcon from '../../assets/comment-icon.png';
import WordCloud from 'react-d3-cloud';
import GraphImg from '../../assets/imgs/graph.svg';

export default function PostAnalysisPage() {
    const mediaList = data.result.mediaList.reportMedias;
    const detailData = data.result;

    const wordCloudData = detailData.tagList.tags.map((word) => ({ text: word.name, value: 1000 }));
    const adPostRatio = detailData.adPostRatio || 50; // 광고 게시글 비율

    return (
        <PostAnalysisWrapper>
            <Section>
                <SectionTitle>인기 포스트</SectionTitle>
                <PostSection>
                    {mediaList.map((post) => (
                        <Post key={post.mediaId}>
                            <PostImage src={post.imageURL} alt="게시글" />
                            <PostStats>
                                <StatItem>
                                    <img src={likeIcon} alt="좋아요 아이콘" />
                                    <StatText>{post.likeCnt}</StatText>
                                </StatItem>
                                <StatItem>
                                    <img src={commentIcon} alt="댓글 아이콘" />
                                    <StatText>{post.replyCnt}</StatText>
                                </StatItem>
                            </PostStats>
                        </Post>
                    ))}
                </PostSection>
            </Section>
            <Section>
                <SectionTitle>상세 분석</SectionTitle>
                <AnalysisWrapper>
                    <WordCloudSection>
                        <Label>게시글 해시태그</Label>
                        <WordCloud
                            data={wordCloudData}
                            fontSizeMapper={
                                (word) => Math.log2(word.value) * 5 + 15 // font-size 조정
                            }
                            rotate={() => 0}
                            fill="#4A3AFF" // 글씨 색상 지정
                        />
                    </WordCloudSection>
                    <ReactionIndexSection>
                        <Label>반응지수</Label>
                        <Reaction>
                            <ReactionData>{detailData.reactionCnt}% EGR</ReactionData>
                            <Description>
                                동일 팔로워군
                                <br />
                                비교 그래프
                            </Description>
                        </Reaction>
                        <ReactionDescription>게시글에 평균 100개의 좋아요를 받아요.</ReactionDescription>
                        <ReactionDescription>게시글에 평균 10개의 댓글을 받아요.</ReactionDescription>
                    </ReactionIndexSection>
                </AnalysisWrapper>
            </Section>
            <Section>
                <AverageStatsWrapper>
                    <StatBox>
                        <Label>
                            전체 게시글의
                            <br />
                            평균 좋아요
                        </Label>
                        <StatContent>
                            <img src={likeIcon} alt="좋아요 아이콘" />
                            <DataValue>{detailData.likeAvg}</DataValue>
                        </StatContent>
                    </StatBox>
                    <StatBox>
                        <Label>
                            전체 게시글의
                            <br />
                            평균 댓글
                        </Label>
                        <StatContent>
                            <img src={commentIcon} alt="댓글 아이콘" />
                            <DataValue>{detailData.replyAvg}</DataValue>
                        </StatContent>
                    </StatBox>
                    <StatBox>
                        <Label>
                            최근 게시글의
                            <br />
                            평균 좋아요
                        </Label>
                        <StatContent>
                            <img src={likeIcon} alt="최근 게시글의 좋아요 평균 아이콘" />
                            <DataValue>{detailData.recentLikeAvg}</DataValue>
                        </StatContent>
                    </StatBox>
                    <StatBox>
                        <Label>
                            최근 게시글의
                            <br />
                            평균 댓글
                        </Label>
                        <StatContent>
                            <img src={commentIcon} alt="최근 게시글의 댓글 평균 아이콘" />
                            <DataValue>{detailData.recentReplyAvg}</DataValue>
                        </StatContent>
                    </StatBox>
                </AverageStatsWrapper>
            </Section>
            <GraphWrapper>
                <GraphBox>
                    <Label>광고 게시글 비율</Label>
                    <Circle>
                        <CircleText>{adPostRatio}%</CircleText>
                    </Circle>
                </GraphBox>
                <GraphBox>
                    <Label>댓글 분석1</Label>
                    <GraphImage src={GraphImg} alt="댓글 분석1" />
                </GraphBox>
                <GraphBox>
                    <Label>댓글 분석2</Label>
                    <GraphImage src={GraphImg} alt="댓글 분석2" />
                </GraphBox>
            </GraphWrapper>
        </PostAnalysisWrapper>
    );
}

const PostAnalysisWrapper = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    min-width: 1000px;
    padding: 40px;
    box-sizing: border-box;
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
    grid-template-columns: repeat(3, 1fr); /* 12-columns 기준 3열 사용 */
    gap: 20px;
`;

const Post = styled.div`
    border-radius: 20px;
    background-color: #fff;
    padding: 10px;
    text-align: center;
`;

const PostImage = styled.img`
    width: 250px;
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
    color: #666;
`;

const AnalysisWrapper = styled.div`
    display: grid;
    grid-template-columns: 7fr 7fr; /* 12-columns 기준 7열 + 7열 사용 */
    gap: 20px;
`;

const WordCloudSection = styled.div`
    padding-top: 20px;
    border-radius: 20px;
    padding-bottom: 30px;
    background-color: #fff;
    height: 350px;
`;

const ReactionIndexSection = styled.div`
    padding: 20px;
    border-radius: 20px;
    background-color: #fff;
    text-align: center;
`;

const Label = styled.h3`
    color: #000;
    text-align: center;
    font-size: 19px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    margin-bottom: 10px;
`;

const ReactionData = styled.p`
    font-size: 24px;
    font-weight: 600;
    color: #7f00ff;
    margin-bottom: 10px;
`;

const Reaction = styled.div`
    display: flex;
    text-align: center;
    justify-content: center;
    gap: 50px;
    margin-bottom: 100px;
    margin-top: 30px;
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
const ReactionDescription = styled.p`
    color: #000;
    text-align: center;
    font-size: 19px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const AverageStatsWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 12-columns 기준 4열 사용 */
    gap: 20px;
    height: 150px;
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
    text-align: center;
    font-family: Inter;
    font-size: 32px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;

const GraphWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 12-columns 기준 3열 사용 */
    gap: 20px;
    margin-top: 30px;
`;

const GraphBox = styled.div`
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 20px;
    background-color: #fff;
    text-align: center;
`;

const Circle = styled.div`
    width: 120px;
    margin-top: 50px;
    height: 120px;
    border-radius: 50%;
    background: linear-gradient(90deg, rgba(74, 58, 255, 0.8) 0%, rgba(102, 48, 170, 0.8) 100%);

    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
`;

const CircleText = styled.p`
    font-size: 24px;
    font-weight: 500;
    color: #fff;
`;

const GraphImage = styled.img`
    width: 100%;
    height: auto;
    border-radius: 15px;
`;
