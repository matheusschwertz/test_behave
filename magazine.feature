Feature: Testar a busca por produto no Magazine Luiza

  Scenario: Buscar por um produto
    Given que estou na página inicial do Magazine Luiza
    When eu busco por um produto
    Then vejo os resultados da busca
