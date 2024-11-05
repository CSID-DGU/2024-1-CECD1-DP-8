import React, { createContext, useContext, useState, useEffect } from 'react';

// NavbarContext 생성
const NavbarContext = createContext();

// NavbarProvider 컴포넌트 생성
export const NavbarProvider = ({ children }) => {
    const [navbar, setNavbarState] = useState(null);

    // navbar 상태를 로컬 스토리지에 저장하고 업데이트하는 함수
    const setNavbar = (value) => {
        setNavbarState(value);
        if (value !== null) {
            localStorage.setItem('navbar', value);
        } else {
            localStorage.removeItem('navbar');
        }
    };

    // 컴포넌트가 처음 마운트될 때 로컬 스토리지에서 navbar 상태 불러오기
    useEffect(() => {
        const storedNavbar = localStorage.getItem('navbar');
        if (storedNavbar) {
            setNavbarState(storedNavbar);
        }
    }, []);

    return <NavbarContext.Provider value={{ navbar, setNavbar }}>{children}</NavbarContext.Provider>;
};

// NavbarContext를 사용하는 커스텀 훅 생성
export const useNavbar = () => useContext(NavbarContext);
