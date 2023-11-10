from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMEOUT = 10  # Ajuste o tempo limite de espera conforme necessário

def wait_for_element_visibility(driver, by, selector):
    element = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((by, selector))
    )
    return element

@given('que estou na página inicial do Magazine Luiza')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.magazineluiza.com.br/')

@when('eu busco por um produto')
def step_impl(context):
    search_box = wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '#inpHeaderSearch')
    search_box.send_keys('smartphone')
    search_box.submit()

@then('vejo os resultados da busca')
def step_impl(context):
    wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '.nm-product-img-link')
    
    assert 'smartphone' in context.driver.title.lower(), "A palavra 'smartphone' não está no título da página de resultados"
    
    context.driver.quit()
