import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { Container } from './styles';

export default function Header() {
  const { handleToggleTheme } = useTheme();

  return (
    <Container>
      <h1>JStack's Blog</h1>
      <button type='button' onClick={handleToggleTheme}>
        🌞
      </button>
    </Container>
  );
}
