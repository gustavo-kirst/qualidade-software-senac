# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software
> Projeto: LocalEats
> Integrante: Gustavo Kirst Farias e Silva – 782410027

---

# 1. Plano de Testes

## 1.1 Objetivo

Validar as principais funcionalidades do sistema LocalEats, verificando se atendem aos requisitos esperados e apresentam comportamento consistente para os usuários.

---

## 1.2 Escopo

### O que será testado

* Login/Cadastro
* Busca de restaurantes
* Visualização de restaurantes
* Sistema de avaliações
* Favoritos

### O que NÃO será testado

* Integrações com serviços externos
* Testes de carga e estresse
* Segurança avançada
* Infraestrutura de hospedagem

---

## 1.3 Funcionalidades selecionadas

* Login/Cadastro
* Busca de restaurantes
* Visualização de restaurantes
* Avaliações
* Favoritos

---

## 1.4 Estratégia de Testes

### Tipos de teste

* ☑ Funcional
* ☑ Usabilidade
* ☑ Validação de regras de negócio

### Abordagem

Serão realizados testes manuais baseados em cenários previamente definidos, contemplando cenários de sucesso (happy path) e cenários de erro.

---

## 1.5 Responsáveis

| Nome                         | Responsabilidade                                 |
| ---------------------------- | ------------------------------------------------ |
| Gustavo Kirst Farias e Silva | Planejamento, execução e documentação dos testes |

---

# 2. Casos de Teste

## CT-01 – Login com credenciais válidas

**Pré-condição:**
Usuário cadastrado no sistema.

**Passos:**

1. Acessar a página de login.
2. Informar e-mail válido.
3. Informar senha válida.
4. Clicar em Entrar.

**Dados de entrada:**

* E-mail válido
* Senha válida

**Resultado esperado:**

O usuário é autenticado e redirecionado para a área principal do sistema.

---

## CT-02 – Busca de restaurante por culinária

**Pré-condição:**
Existirem restaurantes cadastrados.

**Passos:**

1. Acessar a página inicial.
2. Selecionar uma categoria de culinária.
3. Executar a busca.

**Dados de entrada:**

* Categoria: Italiana

**Resultado esperado:**

O sistema exibe apenas restaurantes compatíveis com a categoria selecionada.

---

## CT-03 – Adicionar restaurante aos favoritos

**Pré-condição:**
Usuário autenticado.

**Passos:**

1. Abrir um restaurante.
2. Clicar em Favoritar.

**Dados de entrada:**

* Restaurante válido

**Resultado esperado:**

O restaurante é adicionado à lista de favoritos do usuário.

---

## CT-04 – Login com senha inválida

**Pré-condição:**
Usuário cadastrado.

**Passos:**

1. Acessar a tela de login.
2. Informar e-mail válido.
3. Informar senha incorreta.
4. Clicar em Entrar.

**Dados de entrada:**

* E-mail válido
* Senha inválida

**Resultado esperado:**

O sistema impede o acesso e exibe mensagem de erro.

---

## CT-05 – Busca utilizando filtro inexistente

**Pré-condição:**
Sistema disponível.

**Passos:**

1. Acessar a busca.
2. Informar um filtro sem resultados cadastrados.
3. Executar a pesquisa.

**Dados de entrada:**

* Categoria inexistente

**Resultado esperado:**

O sistema informa que não foram encontrados resultados para a pesquisa realizada.

---

# 3. Execução dos Testes

| ID    | Resultado (Passou/Falhou) | Evidência (descrição ou print)                                                                                                                                                                                   |
| ----- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CT-01 | Passou                    | A página inicial carregou normalmente e apresentou todos os elementos esperados sem lentidão perceptível.                                                                                                        |
| CT-02 | Falhou                    | A busca por nome de restaurante não retornou resultados, mesmo para restaurantes existentes. Os filtros de categoria funcionaram corretamente quando utilizados isoladamente.                                    |
| CT-03 | Falhou                    | As informações do restaurante foram carregadas corretamente, incluindo produtos e funcionalidades de carrinho. Entretanto, os botões de Catálogo e Avaliações não apresentaram qualquer ação ao serem acionados. |
| CT-04 | Falhou Parcialmente       | O restaurante foi adicionado aos favoritos corretamente e apareceu na área "Meus Favoritos". Porém, ao retornar para a página do restaurante, o sistema não indicava visualmente que ele já estava favoritado.   |
| CT-05 | Falhou                    | A funcionalidade de avaliações não respondeu ao clique do usuário, impossibilitando a visualização ou interação com avaliações.                                                                                  |

---

# 4. Análise dos Resultados

* Quantidade de testes executados: 5
* Quantidade de testes que passaram: 1
* Quantidade de testes que falharam: 4

## Principais problemas encontrados

* Busca por nome de restaurante não retorna resultados.
* Funcionalidade de avaliações não está operacional.
* Botões relacionados ao catálogo e avaliações não executam ações.
* Inconsistência visual na funcionalidade de favoritos, que não indica corretamente o estado atual do restaurante.

### Análise

Os testes demonstraram que algumas funcionalidades centrais do sistema apresentam problemas relevantes. A busca por restaurantes e o sistema de avaliações são recursos fundamentais para a experiência dos usuários e devem receber alta prioridade de correção.

Também foi identificada uma inconsistência na funcionalidade de favoritos. Embora os dados sejam persistidos corretamente, a interface não reflete o estado atual do restaurante, o que pode gerar dúvidas e retrabalho para o usuário.

Esses resultados reforçam a importância da execução prática dos testes, pois vários problemas só foram identificados durante a utilização real da aplicação.

---

## Conclusão

As funcionalidades básicas de navegação e visualização de restaurantes apresentaram comportamento adequado. Entretanto, foram identificadas falhas importantes em funcionalidades centrais, especialmente na busca por restaurantes e no sistema de avaliações.

Os resultados indicam que o sistema necessita de correções antes de ser considerado totalmente estável para os usuários finais.

---

# 6. Conclusão Geral

* Qualidade geral do sistema testado: regular.
* Principais pontos positivos: carregamento rápido, navegação simples e funcionamento adequado do carrinho e dos favoritos.
* Principais problemas identificados: busca por nome de restaurante, sistema de avaliações e inconsistências na interface dos favoritos.
* Impressão geral: o processo de testes permitiu identificar falhas relevantes que poderiam impactar diretamente a experiência dos usuários e a credibilidade da plataforma.
