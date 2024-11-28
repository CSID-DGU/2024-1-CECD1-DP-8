import React, { useState } from 'react';
import styled from 'styled-components';
import { FaSearch } from 'react-icons/fa';
import { useNavigate } from 'react-router-dom';

export default function SearchBar({ influencers }) {
    const [query, setQuery] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const navigate = useNavigate();

    const handleInputChange = (e) => {
        const inputValue = e.target.value.toLowerCase();
        setQuery(inputValue);

        if (inputValue.length > 0) {
            const filteredSuggestions = influencers.filter(
                (influencer) =>
                    influencer.nickname.toLowerCase().includes(inputValue) ||
                    influencer.name.toLowerCase().includes(inputValue)
            );
            setSuggestions(filteredSuggestions);
        } else {
            setSuggestions([]);
        }
    };

    const handleSuggestionClick = (influencer) => {
        navigate(`/report/${influencer.id}`); // Navigate to the influencer's report page
        setQuery('');
        setSuggestions([]);
    };

    return (
        <SearchContainer>
            <SearchForm>
                <FaSearch style={{ marginRight: '8px', color: '#9E9E9E' }} />
                <SearchInput type="text" placeholder="인플루언서 검색" value={query} onChange={handleInputChange} />
            </SearchForm>
            {suggestions.length > 0 && (
                <SuggestionsList>
                    {suggestions.map((suggestion) => (
                        <SuggestionItem key={suggestion.id} onClick={() => handleSuggestionClick(suggestion)}>
                            <SuggestionImage src={suggestion.profilePictureUrl} alt={suggestion.nickname} />
                            <SuggestionText>
                                <p>{suggestion.nickname}</p>
                                <small>{suggestion.name}</small>
                            </SuggestionText>
                        </SuggestionItem>
                    ))}
                </SuggestionsList>
            )}
        </SearchContainer>
    );
}

const SearchContainer = styled.div`
    position: relative;
    width: 100%;
    max-width: 400px;
    margin: 0 auto 20px;
`;

const SearchForm = styled.div`
    display: flex;
    align-items: center;
    padding: 10px 14px;
    border-radius: 16px;
    border: 1px solid #e0e0e0;
    background: #f8f8f8;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);

    &:hover {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
`;

const SearchInput = styled.input`
    flex: 1;
    border: none;
    outline: none;
    font-size: 13px;
    background: transparent;

    &::placeholder {
        color: #b0b0b0;
    }
`;

const SuggestionsList = styled.ul`
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    max-height: 180px;
    overflow-y: auto;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid #e0e0e0;
    z-index: 1000;
    list-style: none;
    padding: 6px 0;
    margin: 6px 0 0;
`;

const SuggestionItem = styled.li`
    display: flex;
    align-items: center;
    padding: 8px 12px;
    cursor: pointer;
    transition: background-color 0.2s;

    &:hover {
        background-color: #f2f2f2;
    }
`;

const SuggestionImage = styled.img`
    width: 35px;
    height: 35px;
    margin-right: 10px;
    border-radius: 50%;
    object-fit: cover;
`;

const SuggestionText = styled.div`
    p {
        font-size: 18px;
        font-weight: 500;
        margin: 0;
    }

    small {
        font-size: 17px;
        color: #7d7d7d;
    }
`;
