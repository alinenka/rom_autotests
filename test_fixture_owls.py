import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ['236898','236899','236905'])
def test_link(browser, links):
    #
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    browser.implicitly_wait(12)
    ans=browser.find_element(By.CSS_SELECTOR, ".ember-text-area=")
    answer = str(math.log(int(time.time())))
    ans.send_keys(answer)
    wait = WebDriverWait(browser, 12)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    button.click()
    mess=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    assert mess.text=='Correct!',mess