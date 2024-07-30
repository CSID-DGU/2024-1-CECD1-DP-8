import { createGlobalStyle } from 'styled-components';
import { styled } from 'styled-components';
const GlobalStyle = createGlobalStyle`
  *, *::before, *::after {
    margin : 0;
  }

  body {
    font-family: Inter;
  }


`;

export default GlobalStyle;
