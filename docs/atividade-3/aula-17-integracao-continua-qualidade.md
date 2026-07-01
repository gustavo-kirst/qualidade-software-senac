# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrante

- Gustavo Kirst Farias e Silva – Matrícula: 782410027

---

# 1. Repositório da Atividade

| Item | Descrição |
|--------|-----------|
| Nome do repositório | qualidade-software-senac |
| Link do repositório | https://github.com/gustavo-kirst/qualidade-software-senac |

## Estrutura de Diretórios

```text
qualidade-software-senac/
├── .github/
│   └── workflows/
│       └── quality.yml
├── docs/
├── pages/
├── src/
├── tests/
├── features/
└── README.md
```

---

# 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|-----------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Implementar a regra de cálculo do valor total do pedido e validar seu funcionamento por meio de testes automatizados. |
| Link da Issue | Cole aqui o link da Issue nº 1 |

---

# 3. Teste Automatizado

| Item | Descrição |
|--------|-----------|
| Tipo de teste | Unitário |
| Objetivo do teste | Validar o cálculo correto do valor total do pedido. |
| Link para o arquivo do teste | https://github.com/gustavo-kirst/qualidade-software-senac/blob/main/tests/test_pedido.py |

## Código do teste

```python
from src.pedido import calcular_total_pedido
import pytest


def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    assert calcular_total_pedido(itens, 15) == 30


def test_deve_calcular_total_quando_valor_for_igual_ao_minimo():
    itens = [{"preco": 15}]
    assert calcular_total_pedido(itens, 15) == 15


def test_deve_lancar_erro_quando_valor_minimo_nao_for_atingido():
    itens = [{"preco": 10}]

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 15)
```

---

# 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|-----------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | Push e Pull Request |
| Link para o workflow | https://github.com/gustavo-kirst/qualidade-software-senac/blob/main/.github/workflows/quality.yml |
| Link da execução | Cole aqui o link da execução do GitHub Actions |

## Código do workflow

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install pytest
          pip install pytest-playwright
          pip install pytest-bdd

      - name: Instalar navegadores
        run: playwright install chromium

      - name: Executar testes
        run: python -m pytest
```

---

# 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|-------|
| Quantidade de testes executados | 6 |
| Quantidade de testes aprovados | 6 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

# 6. Registro de Defeito

| Item | Descrição |
|--------|-----------|
| Título do defeito | Erro no cálculo do valor total do pedido |
| Severidade | Alta |
| Link da Issue | Cole aqui o link da Issue nº 2 |

O defeito foi simulado alterando a lógica do cálculo do pedido. O problema foi identificado pela falha dos testes automatizados durante a execução da pipeline de Integração Contínua. Após corrigir a implementação, todos os testes voltaram a ser aprovados.

---

# Conclusão

A atividade demonstrou a importância da Integração Contínua para garantir a qualidade do software. A utilização de GitHub Issues, testes automatizados e GitHub Actions permitiu validar automaticamente alterações no projeto, reduzindo a possibilidade de regressões e aumentando a confiabilidade do processo de desenvolvimento.