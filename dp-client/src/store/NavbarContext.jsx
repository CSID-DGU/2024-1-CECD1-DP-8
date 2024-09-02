import React, { createContext, useContext, useState } from 'react';

// NavbarContext 생성
const NavbarContext = createContext();

// NavbarProvider 컴포넌트 생성
export const NavbarProvider = ({ children }) => {
    const [navbar, setNavbar] = useState(null);

    return <NavbarContext.Provider value={{ navbar, setNavbar }}>{children}</NavbarContext.Provider>;
};

// NavbarContext를 사용하는 커스텀 훅 생성
export const useNavbar = () => useContext(NavbarContext);
