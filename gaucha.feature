Feature: Testar o site GaúchaZH Esportes

  Scenario: Compartilhar uma notícia
    Given que estou na página de uma notícia
    When eu clico no botão de compartilhamento
    And eu escolho uma opção de compartilhamento
    Then sou redirecionado para a página de compartilhamento
