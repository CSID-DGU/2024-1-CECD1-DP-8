import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import { useSelector, useDispatch } from 'react-redux';
import { setProfiles } from '../../store/slices/profileSlice';
import { addMessage } from '../../store/slices/chatSlice';
import ProfileCard from '../../components/Recommend/ProfileCard';
import SendIcon from '../../assets/send-icon.svg';
import ReloadIcon from '../../assets/reload-icon.svg';

export default function Chat() {
    const dispatch = useDispatch();
    const profiles = useSelector((state) => state.profiles);
    const messages = useSelector((state) => state.chat.messages);
    const [loading, setLoading] = useState(false); // 챗봇 응답 로딩 상태

    // 로컬 스토리지에서 상태 복원
    useEffect(() => {
        const savedMessages = localStorage.getItem('chatMessages');
        if (savedMessages) {
            JSON.parse(savedMessages).forEach((msg) => dispatch(addMessage(msg)));
        }

        const savedProfiles = localStorage.getItem('profiles');
        if (savedProfiles) {
            dispatch(setProfiles(JSON.parse(savedProfiles)));
        }
    }, [dispatch]);

    // 메시지가 변경될 때 로컬 스토리지에 저장
    useEffect(() => {
        localStorage.setItem('chatMessages', JSON.stringify(messages));
    }, [messages]);

    // 프로필 변경 시 로컬 스토리지에 저장
    useEffect(() => {
        localStorage.setItem('profiles', JSON.stringify(profiles));
    }, [profiles]);

    // 메시지 전송 핸들러
    const handleSendMessage = (text) => {
        if (text.trim() !== '') {
            dispatch(addMessage({ type: 'user', text })); // 유저 메시지 추가
            setLoading(true); // 로딩 상태 활성화

            // 챗봇 응답 API 요청
            fetch('/api/chat', {
                method: 'POST',
                body: JSON.stringify({ message: text }),
                headers: { 'Content-Type': 'application/json' },
            })
                .then((res) => res.json())
                .then((response) => {
                    dispatch(addMessage({ type: 'bot', text: response.answer })); // 봇 응답 추가
                    setLoading(false); // 로딩 상태 비활성화
                    fetchInfluencerProfiles(); // 인플루언서 카드 업데이트
                })
                .catch((err) => {
                    console.error(err);
                    setLoading(false);
                });
        }
    };

    // 인플루언서 API 호출
    const fetchInfluencerProfiles = () => {
        fetch('/api/influencer-profiles')
            .then((res) => res.json())
            .then((data) => dispatch(setProfiles(data)))
            .catch(console.error);
    };

    const handleReload = () => {
        window.location.reload();
    };

    return (
        <PageWrapper>
            <LeftSidebar>
                {profiles.map((profile) => (
                    <ProfileCard key={profile.id} profile={profile} />
                ))}
            </LeftSidebar>
            <ChatWrapper>
                <ChatContainer>
                    <Messages>
                        {messages.map((msg, index) => (
                            <Message key={index} isUser={msg.type === 'user'}>
                                {msg.text}
                            </Message>
                        ))}
                        {loading && (
                            <Message isUser={false}>
                                <TypingDots />
                            </Message>
                        )}
                    </Messages>
                    <MessageInput onSend={handleSendMessage} onReload={handleReload} />
                </ChatContainer>
            </ChatWrapper>
        </PageWrapper>
    );
}

const TypingDots = () => (
    <TypingDotsWrapper>
        <Dot />
        <Dot />
        <Dot />
    </TypingDotsWrapper>
);

const TypingDotsWrapper = styled.div`
    display: flex;
    gap: 5px;
    justify-content: flex-start;
`;

const Dot = styled.div`
    width: 8px;
    height: 8px;
    background-color: #ccc;
    border-radius: 50%;
    animation: blink 1.5s infinite ease-in-out;

    &:nth-child(1) {
        animation-delay: 0s;
    }
    &:nth-child(2) {
        animation-delay: 0.2s;
    }
    &:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes blink {
        0%,
        100% {
            opacity: 0.3;
        }
        50% {
            opacity: 1;
        }
    }
`;

const MessageInput = ({ onSend, onReload }) => {
    const [text, setText] = useState('');

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            onSend(text);
            setText('');
        }
    };

    return (
        <InputWrapper>
            <ReloadButton onClick={onReload}>
                <img src={ReloadIcon} alt="Reload" />
            </ReloadButton>
            <Input
                value={text}
                onChange={(e) => setText(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="메시지를 입력하세요..."
            />
            <SendButton
                onClick={() => {
                    onSend(text);
                    setText('');
                }}
            >
                <img src={SendIcon} alt="Send" />
            </SendButton>
        </InputWrapper>
    );
};

// 스타일링
const PageWrapper = styled.div`
    display: flex;
    width: 100vw;
    height: 100vh;
`;

const LeftSidebar = styled.div`
    width: 300px;
    background: #f9f9f9;
    padding: 10px;
    overflow-y: auto;
`;

const ChatWrapper = styled.div`
    flex: 1;
    display: flex;
    justify-content: flex-end;
    padding: 20px;
    background: #f5f5fc;
`;

const ChatContainer = styled.div`
    width: 750px;
    height: 700px;
    border-radius: 30px;
    background: rgba(232, 230, 255, 0.9);
    display: flex;
    flex-direction: column;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    margin-right: 20px;
`;

const Messages = styled.div`
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
    border-radius: 20px;
    box-shadow: inset 0px 2px 6px rgba(0, 0, 0, 0.05);
`;

const Message = styled.div`
    max-width: 70%;
    margin-bottom: 15px;
    padding: 12px 20px;
    font-size: 16px;
    font-weight: 500;
    line-height: 1.5;
    border-radius: 20px;
    color: ${(props) => (props.isUser ? '#FFF' : '#333')};
    background: ${(props) => (props.isUser ? '#8a54ff' : '#FFF')};
    align-self: ${(props) => (props.isUser ? 'flex-end' : 'flex-start')};
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const InputWrapper = styled.div`
    display: flex;
    align-items: center;
    padding: 10px;
    background: #f9f9f9;
    border-radius: 30px;
    border: 1px solid #ddd;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    margin: 20px;
`;

const Input = styled.input`
    flex: 1;
    padding: 12px 20px;
    font-size: 14px;
    border: none;
    border-radius: 20px;
    outline: none;
    background: #fff;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
    margin: 0 10px;
`;

const ReloadButton = styled.button`
    width: 40px;
    height: 40px;
    border: none;
    background: transparent;
    cursor: pointer;

    img {
        width: 100%;
        height: 100%;
    }

    &:hover {
        opacity: 0.8;
    }
`;

const SendButton = styled.button`
    width: 40px;
    height: 40px;
    border: none;
    background: transparent;
    cursor: pointer;

    img {
        width: 100%;
        height: 100%;
    }

    &:hover {
        opacity: 0.8;
    }
`;
