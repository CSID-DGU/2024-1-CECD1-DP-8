import { createGlobalStyle } from 'styled-components';
import reset from 'styled-reset';

//Pretendard 폰트 임포트
import PretendardRegular from '../assets/fonts/Pretendard-Regular.woff2';
import PretendardBold from '../assets/fonts/Pretendard-Bold.woff2';

const GlobalStyles = createGlobalStyle`
  ${reset}

  @font-face {
    font-family: 'Pretendard';
    src: url(${PretendardRegular}) format('woff2'),
         url(${PretendardBold}) format('woff2');
    font-style: normal;
  }

  *, *::before, *::after {
    box-sizing: border-box;
  }


  body {
    font-family: 'Pretendard', sans-serif;
    font-size: 1.6rem; /* 16px */
    line-height: 1.6;
    margin: 0;
    padding: 0;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  ul, ol {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  img {
    max-width: 100%;
    height: auto;
  }

  button {
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
    background: none;
    border: none;
    cursor: pointer;
  }

  input, textarea {
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
    outline: none;
  }

 
  .container {
    margin: 0 auto;
  }


`;

export default GlobalStyles;
