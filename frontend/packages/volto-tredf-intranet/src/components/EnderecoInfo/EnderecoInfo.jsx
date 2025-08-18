import React from 'react';
import { Container } from '@plone/components';

const EnderecoInfo = ({ content }) => {
  const { endereco, complemento, cidade, estado, cep } = content;
  return (
    <Container narrow className={'endereco-info'}>
      {endereco && (
        <Container>
          <span className="endereco">{endereco}</span>
        </Container>
      )}
      {complemento && (
        <Container>
          <span className="complemento">{complemento}</span>
        </Container>
      )}
      {cidade && estado && (
        <Container>
          <span className="cidade">{cidade}</span> {' - '}
          <span className="estado">{estado}</span>
        </Container>
      )}
      {cep && (
        <Container>
          <span className="cep">{cep}</span>
        </Container>
      )}
    </Container>
  );
};

export default EnderecoInfo;
