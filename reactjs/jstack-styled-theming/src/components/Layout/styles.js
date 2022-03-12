import styled from 'styled-components';

export const Nav = styled.nav`
  background: ${(props) => props.theme.cardBackgroundColor};
  margin-top: 16px;
  padding: 16px;
  border-radius: ${(props) => props.theme.borderRadius};

  a {
    color: ${(props) => props.theme.textColor};
    text-decoration: none;

    & + a {
      margin-left: 16px;
    }
  }
`;
