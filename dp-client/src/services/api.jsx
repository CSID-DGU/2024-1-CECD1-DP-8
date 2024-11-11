import axios from 'axios';

// 베이스 URL 수정
const api = axios.create({
    baseURL: 'https://influencerdp.shop', // API의 베이스 URL
    headers: {
        'Content-Type': 'application/json',
    },
});

// API 요청 함수들
export const fetchData = async (endpoint, params = {}) => {
    try {
        const response = await api.get(endpoint, { params });
        return response.data;
    } catch (error) {
        if (error.response) {
            // 서버가 응답을 했으나, 응답 코드가 2xx가 아님
            console.error('응답 에러:', error.response.status, error.response.data);
        } else if (error.request) {
            // 요청이 만들어졌으나 응답을 받지 못함
            console.error('요청 오류:', error.request);
        } else {
            // 다른 에러
            console.error('설정 오류:', error.message);
        }
        throw error;
    }
};

// POST 요청 함수
export const postData = async (endpoint, data = {}, config = {}) => {
    try {
        const response = await api.post(endpoint, data, config);
        return response.data;
    } catch (error) {
        console.error(`POST 요청 실패: ${endpoint}`, error);
        throw error;
    }
};

export const updateData = async (endpoint, data = {}) => {
    try {
        const response = await api.put(endpoint, data);
        return response.data;
    } catch (error) {
        console.error(`PUT 요청 실패: ${endpoint}`, error);
        throw error;
    }
};

export const deleteData = async (endpoint) => {
    try {
        const response = await api.delete(endpoint);
        return response.data;
    } catch (error) {
        console.error(`DELETE 요청 실패: ${endpoint}`, error);
        throw error;
    }
};
