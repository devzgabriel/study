import styled from 'styled-components';

export const Container = styled.footer`
  background: ${(props) => props.theme.cardBackgroundColor};
  height: 70px;
  display: flex;
  align-items: center;
  padding: 0 24px;
  border-radius: ${(props) => props.theme.borderRadius};
  justify-content: space-between;
  margin-top: 24px;

  button {
    cursor: pointer;
    background: transparent;
    border: none;
  }
`;
