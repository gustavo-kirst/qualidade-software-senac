# Aula 12 – BDD e Automação Orientada a Comportamento

## 👤 Integrante

- Gustavo Kirst Farias e Silva - 782410027

---

# 🔹 1. Fluxo escolhido

## Fluxo

Visualização de restaurante

### Objetivo

Validar se o usuário consegue acessar a página de detalhes de um restaurante após realizar login e selecionar um estabelecimento.

---

# 🔹 2. Cenários BDD

## Arquivo

```text
features/visualizacao_restaurante.feature
```

## Conteúdo

```gherkin
Feature: Visualização de restaurante

  Scenario: Abrir detalhes de um restaurante
    Given que o usuário acessa a página de login
    When realizar login com credenciais válidas
    And selecionar um restaurante
    Then o sistema deve exibir a página de detalhes do restaurante

  Scenario: Visualizar informações do restaurante
    Given que o usuário está na página de detalhes do restaurante
    When visualizar as informações disponíveis
    Then o nome do restaurante deve estar visível
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
features/
│
└── visualizacao_restaurante.feature

pages/
│
└── restaurante_page.py

tests/
│
├── test_restaurante.py
└── test_bdd_restaurante.py
```

### Tecnologias utilizadas

- Python
- Pytest
- pytest-bdd
- Playwright

---

# 🔹 4. Execução dos testes

## Comando executado

```bash
python -m pytest -v
```

## Resultado

```text
============================= test session starts =============================

6 passed in 7.35s

==========================================================================
```

---

# 🔹 5. Análise crítica

### O cenário ficou legível?

Sim. A estrutura Given-When-Then descreve claramente o comportamento esperado da funcionalidade.

### O teste automatizado ficou legível?

Sim. A separação entre os cenários BDD e a implementação em Python facilitou a leitura e manutenção.

### O BDD ajudou a entender o comportamento?

Sim. Os cenários representam as ações do usuário de forma simples e compreensível.

### Quais dificuldades surgiram?

- Configuração inicial do pytest-bdd.
- Ajuste dos seletores do Playwright.
- Implementação dos steps necessários para cada cenário.

### Os seletores foram frágeis?

Inicialmente sim. Foi necessário utilizar um seletor mais específico (`#restName`) para evitar conflitos.

### O teste ficou dependente da interface?

Sim. Alterações na estrutura HTML ou nos identificadores da página podem exigir atualização dos testes.

### O cenário representa uma regra de negócio?

Sim. Ele valida o comportamento esperado do usuário ao acessar os detalhes de um restaurante.

### O que tornaria o teste mais robusto?

- Utilização de atributos específicos para testes (data-testid).
- Redução da dependência de textos da interface.
- Maior reutilização dos componentes Page Object.

---

# 🔹 6. Reflexão

### O BDD melhora a comunicação entre a equipe?

Sim. Os cenários podem ser compreendidos tanto por desenvolvedores quanto por analistas e pessoas de negócio.

### Todo teste deve utilizar BDD?

Não. O BDD é mais indicado para funcionalidades importantes do ponto de vista do negócio.

### Quando vale a pena utilizar BDD?

Quando é necessário documentar claramente o comportamento esperado do sistema e facilitar a comunicação entre todos os envolvidos.

### Como isso ajuda no projeto?

Permite documentar requisitos de forma executável, facilitando a manutenção dos testes e aumentando a confiança na evolução do sistema.

---

# ✅ Conclusão

A atividade permitiu aplicar conceitos de Behavior-Driven Development utilizando Gherkin, pytest-bdd e Playwright. Os cenários foram automatizados com sucesso e todos os testes executados passaram corretamente, demonstrando que o comportamento esperado do sistema foi validado.