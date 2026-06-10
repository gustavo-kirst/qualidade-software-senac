    # 🧪 Aula 5 – Testes Funcionais vs Estruturais

## LocalEats

---

## 👥 Integrante

* Gustavo Kirst Farias e Silva – 782410027

---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**
Busca de restaurantes

**Descrição da funcionalidade:**
A funcionalidade permite que o usuário encontre restaurantes utilizando filtros como tipo de culinária, localização e faixa de preço.

**O que o usuário espera:**
O usuário espera que a busca retorne restaurantes compatíveis com os critérios informados de forma rápida e precisa.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

* Cenário 1:
  Buscar restaurantes italianos e verificar se os resultados pertencem à categoria selecionada.

* Cenário 2:
  Buscar restaurantes utilizando localização válida e verificar se os resultados estão dentro da região escolhida.

* Cenário 3:
  Buscar restaurantes utilizando uma faixa de preço específica e verificar se os estabelecimentos exibidos correspondem ao filtro.

* Cenário 4:
  Realizar uma busca sem informar filtros e verificar se o sistema apresenta resultados válidos.

---

### 🔹 Possíveis erros identificados

* Restaurantes incompatíveis com os filtros selecionados.
* Ausência de resultados mesmo existindo restaurantes cadastrados.
* Lentidão excessiva durante a busca.
* Resultados duplicados ou incompletos.

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética

```pseudo
Receber filtros informados pelo usuário

Se filtro de culinária existir
    aplicar filtro de culinária

Se filtro de localização existir
    aplicar filtro de localização

Se filtro de preço existir
    aplicar filtro de preço

Consultar banco de dados

Retornar lista de restaurantes encontrados
```

### 🔹 Situações a serem testadas

* Situação 1:
  Verificar se todos os caminhos condicionais (if) são executados corretamente.

* Situação 2:
  Verificar o comportamento quando filtros nulos ou vazios são recebidos.

* Situação 3:
  Validar consultas ao banco de dados e tratamento de erros.

---

### 🔹 Possíveis erros identificados

* Falhas na lógica de aplicação dos filtros.
* Erros de consulta ao banco de dados.
* Condições não tratadas no código.
* Problemas de desempenho causados por consultas ineficientes.

---

## ⚖️ 4. Comparação entre as abordagens

### Qual a principal diferença entre testar sem ver o código e com acesso ao código?

Nos testes caixa-preta o foco está no comportamento externo da funcionalidade, avaliando se o sistema atende às expectativas do usuário. Nos testes caixa-branca o foco está na estrutura interna do software, analisando regras, decisões e fluxos implementados no código.

### Que tipo de problema cada abordagem ajuda a encontrar?

**Caixa-preta:**

* Erros funcionais visíveis ao usuário.
* Problemas de usabilidade.
* Resultados incorretos.
* Falhas nos fluxos de negócio.

**Caixa-branca:**

* Erros de lógica.
* Condições não testadas.
* Problemas de cobertura de código.
* Falhas internas que podem não ser percebidas imediatamente pelo usuário.

---

## 💡 5. Reflexão no contexto do LocalEats

### Qual abordagem parece mais importante neste momento do projeto?

Considerando os problemas relatados pelos usuários, os testes caixa-preta possuem grande importância neste momento, pois permitem validar diretamente os comportamentos observados em produção, como buscas incorretas, lentidão e inconsistências.

### Apenas uma abordagem seria suficiente? Por quê?

Não. As duas abordagens são complementares. Os testes caixa-preta ajudam a verificar se o sistema atende às necessidades dos usuários, enquanto os testes caixa-branca permitem identificar problemas internos que podem causar falhas futuras. Utilizar apenas uma abordagem reduziria a capacidade de identificar defeitos de forma completa.

---

## 🚀 Conclusão

A atividade demonstrou que testes funcionais e estruturais possuem objetivos diferentes, mas complementares. Enquanto os testes caixa-preta avaliam a experiência do usuário e o comportamento esperado do sistema, os testes caixa-branca analisam a implementação interna. A combinação das duas abordagens aumenta a capacidade de identificar defeitos e contribui para uma maior qualidade do software.
