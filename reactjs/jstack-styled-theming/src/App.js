import React from 'react';
import Layout from './components/Layout';
import { ThemeProvider } from './contexts/ThemeContext';
import GlobalStyle from './styles/global';

function App() {
  return (
    <ThemeProvider>
      <GlobalStyle />
      <Layout />
    </ThemeProvider>
  );
}

export default App;
