import React from 'react';
import { Container } from '@plone/components';

const ContactInfo = ({ content }) => {
  const { telefone, email } = content;

  return (
    <Container narrow className="contato">
      <Container className="telefone">
        <span>Telefone</span>: <span>{telefone}</span>
      </Container>
      <Container className="email">
        <span>E-mail</span>: <a href={`mailto:${email}`}>{email}</a>
      </Container>
    </Container>
  );
};

export default ContactInfo;
