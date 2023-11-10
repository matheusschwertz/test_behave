Feature: Verificar se ao clicar em uma notícia o usuário é direcionado para outra página

  Scenario: Clicar em uma notícia
    Given que estou na página inicial do UOL Esporte
    When clico em uma notícia
    Then sou direcionado para outra página
