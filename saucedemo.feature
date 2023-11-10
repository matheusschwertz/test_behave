Feature: Testar o login no Sauce Demo

  Scenario: Fazer login com sucesso
    Given que estou na página de login do Sauce Demo
    When eu insiro minhas credenciais
    And clico no botão de login
    Then sou redirecionado para a página principal
