# PBL 1 – Diagnóstico Inicial da Qualidade do LocalEats

## Integrante

* Gustavo Kirst Farias e Silva - 782410027

---

# 1. Compreensão do Cenário

O LocalEats é uma plataforma web e mobile que conecta moradores e turistas a restaurantes independentes da cidade. O sistema permite buscar restaurantes, visualizar cardápios, salvar favoritos, receber recomendações personalizadas e compartilhar experiências.

Após o lançamento da primeira versão, diversos problemas foram relatados pelos usuários, indicando possíveis falhas em atributos de qualidade do software.

---

# 2. Problemas Identificados e Atributos de Qualidade Afetados

| Problema identificado                             | Atributo de qualidade afetado (ISO/IEC 25010) | Justificativa técnica                                                                            | Impacto para usuário/negócio                                                  |
| ------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Sistema lento em horários de pico                 | Eficiência de Desempenho                      | O sistema apresenta tempo de resposta elevado quando muitos usuários o utilizam simultaneamente. | Usuários podem abandonar a plataforma e procurar concorrentes.                |
| Telas confusas e pouco intuitivas                 | Usabilidade                                   | A interface dificulta a compreensão das funcionalidades e a navegação.                           | Aumenta a frustração e reduz a satisfação do usuário.                         |
| Buscas retornam resultados incorretos             | Adequação Funcional                           | O sistema não entrega resultados compatíveis com os critérios informados pelo usuário.           | Usuários deixam de encontrar restaurantes relevantes.                         |
| Falhas em determinados modelos de smartphone      | Compatibilidade                               | O aplicativo não se comporta corretamente em diferentes dispositivos e ambientes.                | Parte dos usuários não consegue utilizar a aplicação adequadamente.           |
| Dificuldade para concluir ações simples           | Usabilidade                                   | Fluxos importantes exigem esforço excessivo ou são difíceis de compreender.                      | Redução da experiência do usuário e aumento do abandono da plataforma.        |
| Avaliações desaparecem após atualização da página | Confiabilidade                                | O sistema não mantém os dados de forma consistente após operações normais de uso.                | Perda de confiança na plataforma e possível perda de informações importantes. |
| Inconsistências entre versão web e mobile         | Compatibilidade e Adequação Funcional         | Funcionalidades apresentam comportamentos diferentes entre plataformas.                          | Experiência inconsistente e aumento das reclamações dos usuários.             |

---

# 3. Avaliação Geral da Qualidade

Com base nos problemas identificados, o sistema não apresenta um nível de qualidade totalmente adequado para operação sem melhorias.

Os principais atributos comprometidos são:

* Eficiência de Desempenho
* Usabilidade
* Adequação Funcional
* Confiabilidade
* Compatibilidade

Esses problemas afetam diretamente a experiência dos usuários e podem comprometer a reputação do LocalEats junto aos clientes e comerciantes parceiros.

---

# 4. Priorização dos Problemas

## Alta Prioridade

1. Resultados incorretos nas buscas
2. Avaliações desaparecendo
3. Lentidão em horários de pico

### Justificativa

Esses problemas afetam diretamente a funcionalidade principal do sistema, a confiabilidade dos dados e a experiência dos usuários.

## Média Prioridade

1. Falhas em determinados smartphones
2. Inconsistências entre web e mobile
3. Dificuldade para concluir ações simples

### Justificativa

Afetam grupos específicos de usuários e prejudicam a consistência da plataforma.

## Baixa Prioridade

1. Telas confusas

### Justificativa

Embora impactem a experiência do usuário, normalmente não impedem o funcionamento do sistema.

---

# 5. Conclusão

A análise inicial indica que o LocalEats possui problemas relevantes em diversos atributos de qualidade definidos pela ISO/IEC 25010. As maiores preocupações estão relacionadas à adequação funcional, confiabilidade e desempenho, pois afetam diretamente a capacidade do sistema de atender às necessidades dos usuários.

Recomenda-se priorizar a correção das buscas incorretas, da perda de avaliações e da lentidão da aplicação antes da expansão da plataforma ou da realização de novos eventos de grande porte.
