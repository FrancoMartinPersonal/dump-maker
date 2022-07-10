import selenium
from driver.driver_chrome import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import wait_for_element_by_condition


def create_repo(DUMP):
    print('creating a repo...')
    new_repo_xpath = (By.XPATH, "//a[@class='text-center btn btn-primary ml-3']")

    wait_for_element_by_condition(new_repo_xpath,EC.presence_of_element_located)
    new_repo = driver.find_element(*new_repo_xpath)
    new_repo.click()


    