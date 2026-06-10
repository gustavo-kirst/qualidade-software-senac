# Estratégia Inicial de Testes – LocalEats

> Disciplina: Qualidade de Software
> Aula 4 – Estratégia Inicial de Testes
> Integrante: Gustavo Kirst Farias e Silva – 782410027

---

# 1. Funcionalidades

As principais funcionalidades identificadas no sistema LocalEats são:

* Busca de restaurantes
* Login e cadastro de usuários
* Visualização de cardápios
* Sistema de avaliações
* Favoritos
* Recomendações personalizadas

---

# 2. Níveis de Teste

## Funcionalidade: Busca de restaurantes

* **Teste unitário:** validação dos filtros de busca (culinária, localização e faixa de preço).
* **Teste de integração:** comunicação entre sistema de busca e banco de dados.
* **Teste de sistema:** pesquisa completa retornando restaurantes compatíveis.
* **Teste de aceitação:** usuário encontra restaurantes conforme os critérios informados.

---

## Funcionalidade: Login e cadastro

* **Teste unitário:** validação de campos obrigatórios, e-mail e senha.
* **Teste de integração:** autenticação com banco de dados.
* **Teste de sistema:** fluxo completo de cadastro e login.
* **Teste de aceitação:** usuário consegue acessar sua conta com sucesso.

---

## Funcionalidade: Visualização de cardápios

* **Teste unitário:** carregamento correto das informações do cardápio.
* **Teste de integração:** recuperação dos dados do restaurante.
* **Teste de sistema:** exibição completa de cardápio, fotos e informações.
* **Teste de aceitação:** usuário consegue visualizar o conteúdo sem erros.

---

## Funcionalidade: Avaliações

* **Teste unitário:** validação de nota e comentário.
* **Teste de integração:** armazenamento e recuperação das avaliações.
* **Teste de sistema:** usuário publica e visualiza avaliações.
* **Teste de aceitação:** avaliação permanece disponível após atualização da página.

---

## Funcionalidade: Favoritos

* **Teste unitário:** adicionar e remover favoritos.
* **Teste de integração:** sincronização com o perfil do usuário.
* **Teste de sistema:** gerenciamento completo da lista de favoritos.
* **Teste de aceitação:** usuário consegue salvar e consultar restaurantes favoritos.

---

## Funcionalidade: Recomendações personalizadas

* **Teste unitário:** aplicação das regras de recomendação.
* **Teste de integração:** uso dos dados do usuário e restaurantes.
* **Teste de sistema:** geração das recomendações na tela inicial.
* **Teste de aceitação:** usuário recebe sugestões compatíveis com seu perfil.

---

# 3. Prioridades e Riscos

## Alta prioridade

### Busca de restaurantes

É a principal funcionalidade da plataforma. Resultados incorretos comprometem diretamente o objetivo do sistema.

### Login e cadastro

Sem autenticação adequada, o usuário não consegue acessar recursos personalizados.

### Avaliações

A perda de avaliações afeta a confiabilidade da plataforma e a confiança dos usuários.

---

## Média prioridade

### Visualização de cardápios

Importante para a tomada de decisão dos usuários, mas não impede completamente o uso do sistema.

### Recomendações personalizadas

Agregam valor à experiência, porém não são essenciais para a operação básica.

---

## Baixa prioridade

### Favoritos

Melhora a experiência do usuário, mas sua indisponibilidade não impede o uso das demais funcionalidades.

---

# 4. Pirâmide de Testes

## Maior foco: Testes Unitários

Os testes unitários devem representar a maior parte da estratégia por serem rápidos, baratos e capazes de identificar falhas logo no início do desenvolvimento.

## Médio foco: Testes de Integração

Devem validar a comunicação entre componentes importantes, como banco de dados, autenticação e mecanismos de busca.

## Menor foco: Testes de Sistema e Aceitação

São mais custosos e demorados, devendo ser utilizados para validar fluxos completos e experiências reais do usuário.

### Justificativa

A pirâmide de testes permite encontrar defeitos de forma mais eficiente e econômica, reduzindo custos de correção e aumentando a confiabilidade do sistema.

---

# 5. Testes em Produção

O uso de testes em produção pode ser adotado de forma controlada.

### Situações recomendadas

* Monitoramento de desempenho em horários de pico
* Testes A/B para novas funcionalidades
* Monitoramento de erros em diferentes dispositivos móveis
* Verificação de disponibilidade dos serviços

### Justificativa

Alguns problemas só aparecem em ambiente real, principalmente relacionados a carga de usuários, diversidade de dispositivos e comportamento dos clientes. Entretanto, os testes em produção devem complementar os testes realizados em ambientes controlados, e não substituí-los.

---

# Conclusão

A estratégia proposta prioriza as funcionalidades mais críticas do LocalEats, utilizando diferentes níveis de teste para identificar defeitos o mais cedo possível. A aplicação da pirâmide de testes e o uso controlado de testes em produção contribuem para aumentar a qualidade, reduzir riscos e melhorar a experiência dos usuários.
