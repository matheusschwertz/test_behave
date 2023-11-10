from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMEOUT = 10

def wait_for_element_visibility(driver, by, selector):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((by, selector))
    )

def wait_for_url_change(driver, current_url):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.url_changes(current_url)
    )

@given('que estou na página inicial do UOL Esporte')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.uol.com.br/esporte/')

@when('clico em uma notícia')
def step_impl(context):
    wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '.thumbnail')
    context.driver.find_element_by_css_selector('.thumbnail').click()

@then('sou direcionado para outra página')
def step_impl(context):
    current_url = context.driver.current_url
    wait_for_url_change(context.driver, current_url)

    assert 'uol.com.br/esporte/' not in context.driver.current_url, "Não fui redirecionado para outra página"
    
    context.driver.quit()
