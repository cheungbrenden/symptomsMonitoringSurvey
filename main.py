from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from sys import argv
import os
from time import sleep

load_wait_time = 10
opts = Options()

def debug_log(text):
    print('DEBUG: ' + text)

def wait_until_clickable(button, find, custom_wait=load_wait_time):
    return WebDriverWait(driver, custom_wait).until(EC.element_to_be_clickable((find, button)))

driver = Firefox(options=opts)
driver.get('https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7')
wait_until_clickable("//*[@id='QID3-2-label']", By.XPATH).click()
wait_until_clickable("//*[@id='NextButton']", By.XPATH).click()

debug_log("enter credentials")
wait_until_clickable('logon', By.ID).send_keys('cheungbrenden')
wait_until_clickable('pass', By.ID).send_keys('D2IbT2Di()')
wait_until_clickable('primary-button', By.CLASS_NAME).click()

debug_log("click send push")
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
send_push_xpath = '/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button'
wait_until_clickable(send_push_xpath, By.XPATH).click()
driver.switch_to.default_content()


wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
sleep(1)
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
wait_until_clickable('//*[@id="QID221-15-label"]', By.XPATH).click()
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
sleep(1)
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
sleep(1)
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
sleep(1)
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
wait_until_clickable('//*[@id="QID2-1-label"]', By.XPATH).click()
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
wait_until_clickable('//*[@id="QID3-2-label"]', By.XPATH).click()
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
wait_until_clickable('//*[@id="QID12-2-label"]', By.XPATH).click()
wait_until_clickable('//*[@id="NextButton"]', By.XPATH).click()
