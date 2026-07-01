# Aula 9 – Testes Unitários Automatizados e TDD

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante: Gustavo Kirst Farias e Silva – 782410027

---

# 📁 Estrutura do Projeto

```text
.
├── src/
│   └── pedido.py
└── tests/
    └── test_pedido.py
```

---

# 1. Funcionalidade Escolhida

## Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `/src/pedido.py`

**Arquivo de testes:** `/tests/test_pedido.py`

### Descrição

A função calcula o valor total dos itens de um pedido e verifica se o valor mínimo exigido pelo restaurante foi atingido.

### Regras de negócio

- O total do pedido corresponde à soma dos preços dos itens.
- Se o total for menor que o valor mínimo, o sistema deve gerar um erro.
- Caso contrário, o pedido é considerado válido.

---

# 2. Testes Unitários

## Teste 1 – Valor acima do mínimo

**Nome do teste**

`test_deve_calcular_total_quando_valor_minimo_atingido`

**Cenário**

Pedido com valor superior ao mínimo.

**Dados de entrada**

```python
itens = [{"preco": 10}, {"preco": 20}]
valor_minimo = 15
```

**Resultado esperado**

Retornar `30`.

**Resultado obtido**

Passou.

---

## Teste 2 – Valor igual ao mínimo

**Nome do teste**

`test_deve_calcular_total_quando_valor_for_igual_ao_minimo`

**Cenário**

Pedido exatamente no valor mínimo.

**Dados de entrada**

```python
itens = [{"preco": 10}, {"preco": 10}]
valor_minimo = 20
```

**Resultado esperado**

Retornar `20`.

**Resultado obtido**

Passou.

---

## Teste 3 – Valor abaixo do mínimo

**Nome do teste**

`test_deve_lancar_erro_quando_valor_minimo_nao_for_atingido`

**Cenário**

Pedido abaixo do valor mínimo.

**Dados de entrada**

```python
itens = [{"preco": 5}, {"preco": 5}]
valor_minimo = 20
```

**Resultado esperado**

Gerar uma exceção `ValueError`.

**Resultado obtido**

Passou.

---

# 3. Aplicação do TDD

## 🔴 Red

Primeiramente foi criado o teste antes da implementação da função. Ao executar os testes, ocorreu falha porque a função ainda não existia.

## 🟢 Green

Foi criada uma implementação mínima para que o primeiro teste fosse aprovado.

## 🔵 Refactor

Após validar o funcionamento inicial, a função foi refatorada para calcular dinamicamente o total dos itens e validar corretamente a regra do valor mínimo, mantendo todos os testes aprovados.

---

# 4. Refatoração

As seguintes melhorias foram realizadas:

- utilização da função `sum()` para calcular o total;
- melhoria na legibilidade do código;
- tratamento explícito para pedidos abaixo do valor mínimo;
- organização da lógica em uma única função.

---

# 5. Execução dos Testes

## Comando executado

```bash
python -m pytest -v
```

## Resultado

- Total de testes: **3**
- Testes aprovados: **3**
- Testes com falha: **0**

### Evidência

```text
============================= test session starts =============================

tests/test_pedido.py::test_deve_calcular_total_quando_valor_minimo_atingido PASSED
tests/test_pedido.py::test_deve_calcular_total_quando_valor_for_igual_ao_minimo PASSED
tests/test_pedido.py::test_deve_lancar_erro_quando_valor_minimo_nao_for_atingido PASSED

============================== 3 passed ==============================
```

---

# 6. Reflexão

### Foi difícil escrever testes antes do código?

Inicialmente foi necessário mudar a forma de pensar o desenvolvimento, pois normalmente a implementação é realizada antes dos testes.

### O TDD ajudou no desenvolvimento?

Sim. O processo permitiu implementar apenas o necessário para atender aos requisitos e garantiu que a regra de negócio fosse validada continuamente.

### Os testes aumentaram a confiança no código?

Sim. Os testes garantem que alterações futuras na função possam ser verificadas rapidamente, reduzindo a chance de regressões.

### O que poderia ser melhorado?

Seria interessante adicionar novos cenários de teste, como pedidos sem itens, valores inválidos e outros casos de borda.

### Como isso ajuda no projeto LocalEats?

A utilização de testes unitários automatizados aumenta a confiabilidade das regras de negócio e facilita a manutenção do sistema conforme novas funcionalidades forem implementadas.

---

# Conclusão

A atividade permitiu aplicar na prática os conceitos de Test-Driven Development (TDD), desenvolvendo uma função orientada por testes automatizados. A estratégia contribuiu para produzir um código mais organizado, confiável e fácil de manter, demonstrando a importância dos testes unitários na qualidade do software.