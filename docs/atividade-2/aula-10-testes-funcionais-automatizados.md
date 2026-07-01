# Aula 10 – Testes Funcionais Automatizados

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante: Gustavo Kirst Farias e Silva – 782410027

---

# 1. Fluxo Funcional Escolhido

## Fluxo

Visualização de detalhes de um restaurante.

### Descrição

O fluxo permite que o usuário realize login no sistema, acesse a lista de restaurantes e visualize os detalhes de um restaurante específico.

### Importância

Essa funcionalidade faz parte do fluxo principal da aplicação, pois permite ao usuário consultar informações antes de realizar um pedido.

---

# 2. Teste com Codegen

## Comando utilizado

```bash
python -m playwright codegen https://local-eats-unisenac.vercel.app/
```

## Fluxo gravado

- Acessar a página de login.
- Informar e-mail e senha.
- Efetuar login.
- Selecionar um restaurante.
- Abrir a página de detalhes.

## Observações

O Playwright Codegen facilitou a criação inicial do teste, gerando automaticamente os comandos necessários para interação com a interface.

Entretanto, o código gerado apresentou algumas características que exigiram refatoração:

- imports desnecessários;
- criação manual do navegador;
- comandos redundantes;
- baixa reutilização do código.

Esses pontos foram corrigidos posteriormente utilizando boas práticas.

---

# 3. Teste Automatizado com Pytest

## Arquivo

```
tests/test_restaurante.py
```

## Objetivo do teste

O teste realiza automaticamente as seguintes ações:

- acessa o sistema;
- realiza login;
- abre um restaurante;
- valida que a navegação ocorreu corretamente para a página de detalhes.

---

# 4. Refatoração com Page Object Model (POM)

## Arquivo

```
pages/restaurante_page.py
```

## Melhorias realizadas

Após a geração do código pelo Codegen, foi aplicada a arquitetura **Page Object Model (POM)**.

As principais melhorias foram:

- separação entre lógica da interface e lógica do teste;
- reutilização dos métodos;
- código mais limpo;
- maior facilidade de manutenção;
- melhor organização do projeto.

---

# 5. Execução dos Testes

## Comando executado

```bash
python -m pytest -v
```

## Resultado

- Total de testes executados: **4**
- Testes aprovados: **4**
- Testes com falha: **0**

## Evidência

```text
tests/test_pedido.py::test_deve_calcular_total_quando_valor_minimo_atingido PASSED
tests/test_pedido.py::test_deve_calcular_total_quando_valor_for_igual_ao_minimo PASSED
tests/test_pedido.py::test_deve_lancar_erro_quando_valor_minimo_nao_for_atingido PASSED
tests/test_restaurante.py::test_deve_abrir_detalhes_do_restaurante[chromium] PASSED

======================== 4 passed ========================
```

---

# 6. Análise Crítica

## O teste quebrou em algum momento?

Sim. Inicialmente a validação verificava se a URL terminava exatamente com `restaurant.html`. Como a aplicação adiciona o parâmetro `?id=1`, a asserção falhou.

A solução foi tornar a validação mais robusta verificando apenas se `"restaurant.html"` está presente na URL.

## Quais seletores foram mais difíceis?

Os seletores relacionados ao login exigiram atenção por utilizarem os textos dos campos da interface.

## O Codegen ajudou?

Sim. O Codegen acelerou a criação inicial da automação, reduzindo o tempo necessário para escrever o teste.

## O teste é confiável?

Sim, porém ainda depende de alguns textos presentes na interface. Alterações nesses textos podem exigir atualização dos seletores.

## O que tornaria o teste mais robusto?

- utilização de atributos específicos (`data-testid`);
- seletores menos dependentes do texto da interface;
- inclusão de novas validações sobre os elementos carregados na página.

## Quais são os riscos de manutenção?

Mudanças na interface ou nos identificadores dos elementos podem exigir ajustes no teste automatizado.

---

# 7. Reflexão

## Testes automatizados substituem testes manuais?

Não. Ambos são importantes e se complementam. Testes automatizados são ideais para validar funcionalidades repetitivas, enquanto testes manuais continuam importantes para usabilidade e testes exploratórios.

## Vale a pena automatizar todos os fluxos?

Não. Devem ser priorizados os fluxos críticos da aplicação, reduzindo o custo de manutenção da suíte de testes.

## Qual tipo de teste deve ser priorizado?

Os testes automatizados devem priorizar funcionalidades essenciais do sistema, como login, navegação, consulta de restaurantes e fluxo de pedidos.

## Como isso ajuda no projeto?

A automação aumenta a confiança nas entregas, reduz regressões e permite validar rapidamente os principais fluxos da aplicação.

---

# Conclusão

A atividade permitiu aplicar testes funcionais automatizados utilizando Playwright, Pytest e o padrão Page Object Model. O processo demonstrou como estruturar automações de forma organizada, reutilizável e mais resistente a mudanças, contribuindo para a melhoria contínua da qualidade do software.