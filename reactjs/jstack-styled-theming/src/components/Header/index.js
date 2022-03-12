import React from 'react';
import { useHistory } from 'react-router-dom';
import { useTheme } from '../../contexts/ThemeContext';
import { Container } from './styles';

export default function Header() {
  const { handleToggleTheme } = useTheme();
  const history = useHistory();

  function handleNavigate() {
    history.push('/posts');
  }

  return (
    <Container>
      <h1>JStack's Blog</h1>
      <button type='button' onClick={handleToggleTheme}>
        🌞
      </button>
      <button style={{ color: '#fff' }} onClick={handleNavigate}>
        Navegar
      </button>
    </Container>
  );
}
