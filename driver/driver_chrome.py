from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from commons_qa_web.driver.driver_manager import DriverManager
from selenium import webdriver

options = Options()

options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1200")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disk-cache-size=0")
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)