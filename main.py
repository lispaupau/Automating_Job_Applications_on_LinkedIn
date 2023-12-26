import time

import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

login = os.environ.get('login')
password = os.environ.get('password')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    url='https://www.linkedin.com/jobs/search/?currentJobId=3787407575&f_AL=true&keywords=Python-'
        '%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&origin='
        'JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')

time.sleep(5)

driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]').click()

enter_login = driver.find_element(By.ID, value='username')
enter_login.send_keys(login)

enter_pass = driver.find_element(By.ID, value='password')
enter_pass.send_keys(password)

driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()
driver.find_element(By.CLASS_NAME, value='job-card-container').click()
driver.find_element(By.CLASS_NAME, value='jobs-apply-button').click()
driver.find_element(By.CLASS_NAME, value='job-details-easy-apply-footer__section').click()
driver.find_element(By.CLASS_NAME, value='artdeco-button').click()
