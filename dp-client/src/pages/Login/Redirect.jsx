import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const KakaoRedirect = () => {
    const navigate = useNavigate();
    const code = new URL(window.location.href).searchParams.get('code');

    useEffect(() => {
        const headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        };

        if (code) {
            fetch(`http://localhost:3000/api/kakao/callback?code=${code}`, {
                // 백엔드 API 주소로 수정
                method: 'POST',
                headers: headers,
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    // 데이터 처리 (예: 토큰 저장 등)
                    if (data.result && data.result.jwt) {
                        // 토큰을 로컬 스토리지에 저장하거나 상태 관리 라이브러리 사용
                        localStorage.setItem('token', data.result.jwt);
                        navigate('/'); // 로그인 후 리디렉션
                    } else {
                        console.error('로그인 실패');
                    }
                })
                .catch((error) => {
                    console.error('오류 발생', error);
                });
        } else {
            console.error('인가 코드가 없습니다.');
        }
    }, [code, navigate]);

    return (
        <div>
            <h1>로그인 중입니다...</h1>
        </div>
    );
};

export default KakaoRedirect;
