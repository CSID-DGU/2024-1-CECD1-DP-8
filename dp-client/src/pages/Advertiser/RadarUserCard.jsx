import { styled } from 'styled-components';
import { Radar } from 'react-chartjs-2';
import { Chart as ChartJS, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend, Colors } from 'chart.js';
ChartJS.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend);

const categories = {
    뷰티: '#FCA5A5',
    패션: '#FCE9A5',
    스포츠: 'lightblue',
    음식: '#3357FF',
    여행: '#FF33A5',
  };

const RadarUserCard = (data) => {

    const user = data.data;

    const radarData = {
        labels: [
            ['게시글', '해시태그'], 
            ['팔로워수', '조건'], 
            ['팔로워', '참여도'], 
            ['예상', '광고효과'], 
            ['게시글', '키워드']
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [user.postHashTag, user.wantedFollower, user.engagement, user.advertisement, user.postKeyWord],
            fill: true,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)'
        }, 
        /*
        {
            label: 'My Second Dataset',
            data: [28, 48, 40, 19, 96],
            fill: true,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            pointBackgroundColor: 'rgb(54, 162, 235)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
        }
        */
        ]
    };
    const options = {
        elements: {
            line: {
                borderWidth: 3
            }
        },
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            r: {
                min: 0,
                max: 100,
                pointLabels: {
                    font: {
                        size: 16,
                        weight: 'bold'
                    }
                }
            }
        }
    };

    return (
        <CardContainer>
            <MatchText>match {user.matchPercent}%</MatchText>
            <Contents>
                <UserInfoContainer>
                    <UserImage src={user.img} alt="프로필 사진"/>
                    <UserInfo>
                        <UserData>
                            <UserInfoText bold="yes">Username</UserInfoText>
                            <UserInfoText>{user.username}</UserInfoText>
                        </UserData>
                        <UserData>
                            <UserInfoText bold="yes">팔로워</UserInfoText>
                            <UserInfoText>{user.follower}</UserInfoText>
                        </UserData>
                    </UserInfo>
                    <CategoryContainer>
                        <Category category={user.category1}>{user.category1}</Category>
                        <Category category={user.category2}>{user.category2}</Category>
                    </CategoryContainer>
                </UserInfoContainer>
                <RadarWrapper>
                    <Radar data={radarData} options={options} />
                </RadarWrapper>
            </Contents>
        </CardContainer>
    )
}

export default RadarUserCard;

const CardContainer = styled.div`
    display: flex;
    padding: 18px;
    flex-direction: column;
    align-items: flex-start;
    gap: 30px;
    border-radius: var(--20, 20px);
    background: var(--white-100, #FFF);
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
`;

const MatchText = styled.text`
    align-self: stretch;
    font-family: Inter;
    font-size: 18px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
    background: linear-gradient(90deg, #EA6CFF 0%, #BA59F6 20.5%, #4A3AFF 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
`;

const Contents = styled.div`
    display: flex;
    align-items: flex-start;
    gap: 70px;
`;

const UserInfoContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
`;

const UserImage = styled.img`
    display: flex;
    width: 120px;
    height: 123px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 100px;
    border: 0.5px solid #DDD;
    background: transparent;
`;

const UserInfo = styled.div`
    display: flex;
    align-items: flex-start;
    gap: 40px;
`;

const UserData = styled.div`
    display: flex;
    width: auto;
    flex-direction: column;
    align-items: center;
    gap: 12px;
`;

const UserInfoText = styled.text`
    color: #000;
    text-align: center;
    font-feature-settings: 'clig' off, 'liga' off;
    font-family: "DM Sans";
    font-size: ${(props) => (props.bold === 'yes' ? '19px' : '18px')};
    font-style: normal;
    font-weight: ${(props) => (props.bold === 'yes' ? 'bold' : '400')};
    line-height: normal;
`;

const CategoryContainer = styled.div`
    display: flex;
    align-items: flex-start;
    gap: 13px;
`;

const Category = styled.div`
    display: flex;
    width: 57.183px;
    padding: 10px;
    justify-content: center;
    align-items: center;
    gap: 10px;
    border-radius: var(--20, 20px);
    background: ${(props) => (categories[props.category] || "white")};

    color: #000;
    font-family: Inter;
    font-size: 14px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;


const RadarWrapper = styled.div`
    position: relative;
    top: -40px;
`