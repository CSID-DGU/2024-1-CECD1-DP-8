import { createSlice } from '@reduxjs/toolkit';

const profilesSlice = createSlice({
    name: 'profiles',
    initialState: [],
    reducers: {
        setProfiles: (state, action) => action.payload, // 프로필 리스트 설정
    },
});

export const { setProfiles } = profilesSlice.actions;
export default profilesSlice.reducer;
