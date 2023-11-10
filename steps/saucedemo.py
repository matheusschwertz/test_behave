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

@given('que estou na página de login do Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')

@when('eu insiro minhas credenciais')
def step_impl(context):
    username = wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '#user-name')
    password = wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '#password')
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')

@when('clico no botão de login')
def step_impl(context):
    wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '#login-button').click()

@then('sou redirecionado para a página principal')
def step_impl(context):
    wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '.inventory_list')
    
    assert 'inventory' in context.driver.current_url, "A URL não contém 'inventory'"
    
    context.driver.quit()
