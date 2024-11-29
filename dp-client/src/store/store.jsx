// store.js
import { configureStore } from '@reduxjs/toolkit';
import profilesReducer from './slices/profileSlice';
import chatReducer from './slices/chatSlice';

export const store = configureStore({
    reducer: {
        profiles: profilesReducer,
        chat: chatReducer,
    },
});
