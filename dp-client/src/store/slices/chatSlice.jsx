import { createSlice } from '@reduxjs/toolkit';

const chatSlice = createSlice({
    name: 'chat',
    initialState: {
        messages: [], // 채팅 메시지 목록
    },
    reducers: {
        addMessage: (state, action) => {
            state.messages.push(action.payload); // 새로운 메시지 추가
        },
    },
});

export const { addMessage } = chatSlice.actions;
export default chatSlice.reducer;
