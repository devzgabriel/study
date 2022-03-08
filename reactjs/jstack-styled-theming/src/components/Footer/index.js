import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { Container } from './styles';

export default function Footer() {
  const { handleToggleTheme } = useTheme();

  return (
    <Container>
      <span>JStack's Blog. Todos os direitos reservados.</span>
      <button type='button' onClick={handleToggleTheme}>
        🌞
      </button>
    </Container>
  );
}
