import selenium
from driver.driver_chrome import driver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from decouple import config
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from utils.url_to_name import urlRepoName
from utils.base_page import wait_for_element_by_condition
from pages.gh_create_repo import create_repo
from selenium.common.exceptions import TimeoutException



def lookingRepo(DUMP):
    #ActionChains(driver).mo
    # ve_to_element(repo_search).click().perform()

    
   
    repo_search_xpath = (By.XPATH,"//input[@id='your-repos-filter']" )
    repositories_found_xpath = (By.XPATH, "//*[@id='user-repositories-list']/ul/li/div[1]/div[1]/h3/a")
    profile_collapser_xpath = (By.XPATH, "//summary[@aria-label='View profile and more']//span[@class='dropdown-caret']")
    profile_option_your_repositories_xpath = (By.XPATH, "//a[normalize-space()='Your repositories']")
    username_text_xpath = (By.XPATH, "//strong[@class='css-truncate-target']")
    
    

    wait_for_element_by_condition(profile_collapser_xpath,EC.presence_of_element_located)
    profile_collapser = driver.find_element(*profile_collapser_xpath)
    profile_collapser.click()

    #pick the username
    wait_for_element_by_condition(username_text_xpath,EC.presence_of_element_located)
    username_text = driver.find_element(*username_text_xpath)
    username_text_innerText = username_text.get_attribute("innerText")
    print(username_text_innerText, "username_text_innerText") 

    wait_for_element_by_condition(profile_option_your_repositories_xpath,EC.presence_of_element_located)
    profile_option_your_repositories = driver.find_element(*profile_option_your_repositories_xpath)
    profile_option_your_repositories.click()

    wait_for_element_by_condition(repo_search_xpath,EC.presence_of_element_located)
    repo_search = driver.find_element(*repo_search_xpath)
    repo_search.click()
    repo_search.send_keys(DUMP)
    
    def repo_doesnt_found_fun(name):
        return (By.XPATH, f"//h2[contains(text(),'{name} doesn’t have any repositories')]")

    repo_doesnt_found_xpath = repo_doesnt_found_fun(username_text_innerText)


    # get repo name thoughout href
    
    
    try:
        wait_for_element_by_condition(repo_doesnt_found_xpath,EC.presence_of_element_located)
        repo_doesnt_found = driver.find_element(*repo_doesnt_found_xpath)
        print('the repo doesnt exists')
        create_repo(DUMP)
    except TimeoutException:
        print('the repo already exists,go to trasher...')
        wait_for_element_by_condition(repositories_found_xpath,EC.presence_of_element_located)
        repo_found = driver.find_element(*repositories_found_xpath)
        #repo = repo_found.get_attribute("href")
        repo_found.click()

    

    # if not repo_doesnt_found:
    #     print('the repo already exists,go to trash...')
    #     #repositories_found.click()
    # elif(repo_doesnt_found):
    #     print('the repo doesnt exists')
    #     create_repo(DUMP)

    #repositories_found_xpath.click()
    

