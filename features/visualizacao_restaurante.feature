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