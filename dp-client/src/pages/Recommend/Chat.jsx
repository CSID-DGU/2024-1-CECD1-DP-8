import React, { useEffect, useState, useRef } from 'react';
import styled from 'styled-components';
import { useDispatch } from 'react-redux';
import { setProfiles } from '../../store/slices/profileSlice';
import ProfileCard from '../../components/Recommend/ProfileCard';
import SendIcon from '../../assets/send-icon.svg';
import ReloadIcon from '../../assets/reload-icon.svg';
import { fetchData } from '../../services/api';
import { useLocation } from 'react-router-dom';

export default function Chat() {
    const location = useLocation();
    const [messages, setMessages] = useState(
        location.state?.question && location.state?.chatResponse
            ? [
                  { type: 'user', text: location.state.question }, // RecommendPage에서 입력한 질문
                  { type: 'bot', text: location.state.chatResponse }, // RecommendPage에서 전달된 응답
              ]
            : []
    );
    const [influencers, setInfluencers] = useState([]);
    const dispatch = useDispatch();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [inputText, setInputText] = useState('');
    const messagesEndRef = useRef(null);

    const extractInfluencerIds = (responseText) => {
        const idRegex = /id:([a-zA-Z0-9_]+)/g;
        const matches = [...responseText.matchAll(idRegex)];
        return matches.map((match) => match[1]);
    };
    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [messages]);

    const loadInfluencerProfiles = async (ids) => {
        try {
            const promises = ids.map((id) =>
                fetchData(`/influencer/report/${id}`, { period: 'W' }).then((res) => ({
                    ...res.result.profile,
                    allTagsOfMedias: res.result.allTagsOfMedias,
                    id,
                }))
            );

            const results = await Promise.all(promises);
            setInfluencers(results);
        } catch (err) {
            console.error('Error fetching influencer profiles:', err);
        }
    };

    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [messages]);

    useEffect(() => {
        if (messages.length > 0) {
            const lastMessage = messages[messages.length - 1];
            if (lastMessage.type === 'bot') {
                const ids = extractInfluencerIds(lastMessage.text);
                if (ids.length > 0) {
                    loadInfluencerProfiles(ids);
                }
            }
        }
    }, [messages]);

    const handleSendMessage = async (text) => {
        if (text.trim() === '') return;

        const userMessage = { type: 'user', text };
        setMessages((prev) => [...prev, userMessage]);

        try {
            setLoading(true);
            const response = await fetch('https://4e4e-34-87-133-241.ngrok-free.app/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: text }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            const botMessage = { type: 'bot', text: data.result };

            setMessages((prev) => [...prev, botMessage]);

            const ids = extractInfluencerIds(data.result);
            if (ids.length > 0) {
                loadInfluencerProfiles(ids);
            }
        } catch (err) {
            console.error('Error fetching chat response:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleReload = () => {
        window.location.reload();
    };

    return (
        <PageWrapper>
            <LeftSidebar>
                {influencers.map((profile) => (
                    <ProfileCard key={profile.id} profile={profile} />
                ))}
                {error && <ErrorText>{error}</ErrorText>}
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
                        <div ref={messagesEndRef} />
                    </Messages>
                    <InputWrapper>
                        <ReloadButton onClick={handleReload}>
                            <img src={ReloadIcon} alt="Reload" />
                        </ReloadButton>
                        <Input
                            value={inputText}
                            onChange={(e) => setInputText(e.target.value)}
                            onKeyPress={(e) => {
                                if (e.key === 'Enter') {
                                    handleSendMessage(inputText);
                                    setInputText('');
                                }
                            }}
                            placeholder="메시지를 입력하세요..."
                        />
                        <SendButton
                            onClick={() => {
                                handleSendMessage(inputText);
                                setInputText('');
                            }}
                        >
                            <img src={SendIcon} alt="Send" />
                        </SendButton>
                    </InputWrapper>
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

const PageWrapper = styled.div`
    display: flex;
    height: 100vh;
`;

const LeftSidebar = styled.div`
    flex: 1;
    background: #f9f9f9;
    padding: 20px;
    overflow-y: auto;
`;

const ChatWrapper = styled.div`
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 20px 20px 20px;
`;

const ChatContainer = styled.div`
    width: 90%;
    height: 90%;
    border-radius: 30px;
    background: rgba(232, 230, 255, 0.9);
    display: flex;
    flex-direction: column;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const Messages = styled.div`
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
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
    margin: 20px;
`;

const Input = styled.input`
    flex: 1;
    padding: 12px 20px;
    font-size: 14px;
    border: none;
    border-radius: 20px;
    outline: none;
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
`;

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

const ErrorText = styled.div`
    color: red;
    text-align: center;
    margin-top: 20px;
`;
