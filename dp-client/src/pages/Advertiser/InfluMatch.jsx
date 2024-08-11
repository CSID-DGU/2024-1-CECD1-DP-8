import { styled } from 'styled-components';

const InfluMatch = (data) => {
    const user = data.data;
    return (
        <CardContainer>
            <MatchText>match {user.matchPercent}%</MatchText>
            <Contents>
                <UserImage src={user.img} alt="프로필 사진"/>
                <UserInfo>
                    <UserInfoText bold="yes">User</UserInfoText>
                    <UserInfoText>{user.username}</UserInfoText>
                </UserInfo>
                <UserInfo>
                    <UserInfoText bold="yes">팔로워</UserInfoText>
                    <UserInfoText>{user.follower}</UserInfoText>
                </UserInfo>
                <ContentButton background="var(--coral-50)">
                <ButtonText>{user.category}</ButtonText>
                </ContentButton>
                <ContentButton background="var(--violet-50)">
                    <ButtonText>{user.match}</ButtonText>
                </ContentButton>
            </Contents>
        </CardContainer>
    )
}

export default InfluMatch;

const CardContainer = styled.div`
    display: flex;
    height: 163px;
    padding: 5px 0px 0px 30px;
    flex-direction: column;
    align-items: flex-start;
    border-radius: var(--20, 20px);
    background: var(--white-100, #FFF);
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
`;

const MatchText = styled.text`
    width: 112px;
    height: 23px;
    flex-shrink: 0;
    color: #000;
    text-align: center;
    font-feature-settings: 'clig' off, 'liga' off;
    font-family: "DM Sans";
    font-size: 18px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
`;

const Contents = styled.div`
    display: flex;
    width: 803px;
    padding: 10px 20px 20px 0px;
    align-items: center;
    gap: 70px;
    flex: 1 0 0;
    border-radius: var(--20, 20px);
    background: var(--white-100, #FFF);
`;

const UserImage = styled.img`
    display: flex;
    width: 97.087px;
    height: 100px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
    border-radius: 100px;
    border: 0.5px solid #DDD;
    background: transparent;
`;

const UserInfo = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 11px;
    flex: 1 0 0;
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

const ContentButton = styled.button`
    display: flex;
    height: 35px;
    padding: 10px;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex: 1 0 0;
    border: transparent;
    border-radius: var(--20, 20px);
    background: ${(props) => props.background || "white"};
`;

const ButtonText = styled.div`
    color: #000;
    font-family: Inter;
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    letter-spacing: -0.5px;
    text-transform: capitalize;
`;