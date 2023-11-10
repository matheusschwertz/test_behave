from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMEOUT = 10  # Ajuste o tempo limite de espera conforme necessário

def wait_and_click(driver, by, selector):
    element = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable((by, selector))
    )
    element.click()

def wait_for_url_to_contain(driver, expected_text):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.url_contains(expected_text)
    )

@given('que estou na página de uma notícia')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://gauchazh.clicrbs.com.br/esportes/ultimas-noticias/')

@when('eu clico no botão de compartilhamento')
def step_impl(context):
    wait_and_click(context.driver, By.CSS_SELECTOR, '.share-button')

@when('eu escolho uma opção de compartilhamento')
def step_impl(context):
    wait_and_click(context.driver, By.CSS_SELECTOR, '.share-menu-item')

@then('sou redirecionado para a página de compartilhamento')
def step_impl(context):
    wait_for_url_to_contain(context.driver, 'share')
    assert 'share' in context.driver.current_url, "URL não contém 'share'"
    context.driver.quit()
