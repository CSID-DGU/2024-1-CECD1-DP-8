import React, { useEffect, useState, useRef } from 'react';
import styled from 'styled-components';
import { useDispatch } from 'react-redux';
import { setProfiles } from '../../store/slices/profileSlice';
import ProfileCard from '../../components/Recommend/ProfileCard';
import SendIcon from '../../assets/send-icon.svg';
import ReloadIcon from '../../assets/reload-icon.svg';
import { fetchData } from '../../services/api';
import { useLocation } from 'react-router-dom';
import { fetchChatResponse } from '../../services/chatApi';
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
        try {
            const idRegex = /\b(?:id\s*[:：]\s*@?)([a-zA-Z0-9._]+)/g;
            const matches = [...responseText.matchAll(idRegex)];
            const ids = matches.map((match) => match[1]);
            console.log('Extracted IDs:', ids); // 디버깅
            return ids;
        } catch (error) {
            console.error('Error in extractInfluencerIds:', error);
            return [];
        }
    };

    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [messages]);

    const formatMessage = (text) => {
        // 개행 문자를 <br /> 태그로 변환
        return text.split('\n').map((line, index) => (
            <React.Fragment key={index}>
                {line}
                <br />
            </React.Fragment>
        ));
    };
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
            console.log(results);
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

            // fetchChatResponse 함수 호출
            const data = await fetchChatResponse(text);

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
                                {formatMessage(msg.text)}
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
    gap: 10px; /* Left와 Right 사이의 마진 */

    @media (max-width: 768px) {
        flex-direction: column; /* 모바일 화면에서는 세로로 배치 */
        gap: 5px; /* 마진 감소 */
        padding: 5px;
    }
`;

const LeftSidebar = styled.div`
    flex: 1;
    background: #f9f9f9;
    padding: 20px;
    margin-right: 10px;
    overflow-y: auto;
    border-radius: 10px;

    @media (max-width: 768px) {
        flex: none;
        height: 50%; /* 모바일 화면에서 높이 50% */
        padding: 10px;
    }

    @media (max-width: 480px) {
        height: 40%; /* 작은 화면에서는 높이 40% */
        padding: 5px;
    }
`;

const ChatWrapper = styled.div`
    flex: 1; /* Left와 Right가 동일한 비율을 차지 */
    display: flex;

    justify-content: center;
    align-items: center;
    border-radius: 10px;

    @media (max-width: 768px) {
        flex: none;
        height: 50%; /* 모바일 화면에서 높이 50% */
    }

    @media (max-width: 480px) {
        height: 60%; /* 작은 화면에서는 높이 60% */
        padding: 10px;
    }
`;

const ChatContainer = styled.div`
    width: 90%;
    height: 85%;
    margin-top: -50px;
    border-radius: 10px;
    background: rgba(232, 230, 255, 0.9);
    display: flex;
    flex-direction: column;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);

    @media (max-width: 768px) {
        border-radius: 8px;
    }

    @media (max-width: 480px) {
        border-radius: 6px;
    }
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

    @media (max-width: 768px) {
        font-size: 14px;
        padding: 10px 15px;
        border-radius: 15px;
    }

    @media (max-width: 480px) {
        font-size: 12px;
        padding: 8px 12px;
        border-radius: 10px;
    }
`;

const Messages = styled.div`
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;

    @media (max-width: 768px) {
        padding: 15px;
        gap: 8px;
    }

    @media (max-width: 480px) {
        padding: 10px;
        gap: 6px;
    }
`;

const InputWrapper = styled.div`
    display: flex;
    align-items: center;
    padding: 10px;
    background: #f9f9f9;
    border-radius: 30px;
    margin: 20px;

    @media (max-width: 768px) {
        margin: 15px;
        border-radius: 20px;
        padding: 8px;
    }

    @media (max-width: 480px) {
        margin: 10px;
        border-radius: 15px;
        padding: 5px;
    }
`;

const Input = styled.input`
    flex: 1;
    padding: 12px 20px;
    font-size: 14px;
    border: none;
    border-radius: 20px;
    outline: none;

    @media (max-width: 768px) {
        padding: 10px 15px;
        font-size: 13px;
    }

    @media (max-width: 480px) {
        padding: 8px 10px;
        font-size: 12px;
    }
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

    @media (max-width: 768px) {
        width: 30px;
        height: 30px;
    }

    @media (max-width: 480px) {
        width: 25px;
        height: 25px;
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

    @media (max-width: 768px) {
        width: 30px;
        height: 30px;
    }

    @media (max-width: 480px) {
        width: 25px;
        height: 25px;
    }
`;

const TypingDotsWrapper = styled.div`
    display: flex;
    gap: 5px;
    justify-content: flex-start;

    @media (max-width: 480px) {
        gap: 3px;
    }
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

    @media (max-width: 768px) {
        width: 6px;
        height: 6px;
    }

    @media (max-width: 480px) {
        width: 5px;
        height: 5px;
    }
`;

const ErrorText = styled.div`
    color: red;
    text-align: center;
    margin-top: 20px;

    @media (max-width: 768px) {
        margin-top: 15px;
    }

    @media (max-width: 480px) {
        margin-top: 10px;
    }
`;
