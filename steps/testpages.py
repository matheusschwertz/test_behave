from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMEOUT = 10

def wait_for_text_to_be_present(driver, text, by, selector):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.text_to_be_present_in_element((by, selector), text)
    )

def wait_for_element_visibility(driver, by, selector):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((by, selector))
    )

@given('que estou na página inicial Key Click Display')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://testpages.eviltester.com/styled/key-click-display-test.html')

@when('eu clico no botão')
def step_impl(context):
    wait_for_element_visibility(context.driver, By.CSS_SELECTOR, '#key')
    context.driver.find_element_by_css_selector('#key').click()

@then('o texto é exibido na página')
def step_impl(context):
    wait_for_text_to_be_present(context.driver, 'You pressed a key', By.CSS_SELECTOR, 'body')
    
    assert 'You pressed a key' in context.driver.page_source, "O texto 'You pressed a key' não foi exibido"
    
    context.driver.quit()
