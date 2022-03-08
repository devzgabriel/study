import React, { createContext, useMemo, useState, useContext } from 'react';
import { ThemeProvider as SCThemeProvider } from 'styled-components';
import themes from '../styles/themes';

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('dark');
  const currentTheme = useMemo(() => themes[theme] || themes.dark, [theme]);

  function handleToggleTheme() {
    setTheme((prev) => (prev === 'dark' ? 'light' : 'dark'));
  }

  return (
    <ThemeContext.Provider
      value={{
        currentTheme,
        handleToggleTheme,
      }}
    >
      <SCThemeProvider theme={currentTheme}>{children}</SCThemeProvider>
    </ThemeContext.Provider>
  );
}

export const useTheme = () => useContext(ThemeContext);
