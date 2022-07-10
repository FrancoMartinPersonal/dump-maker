import selenium
from driver.driver_chrome import driver
from url.url_manager import url_base,url_login
from decouple import config
#pages
from pages.github_login import  login
from pages.gh_search_repo import lookingRepo
#variables
print(config('USERNAME_GITHUB'))
DUMP = 'budgetMind'
#access github
driver.get(url_login)

#login
login()
driver.get(url_base)

# looking for repo
lookingRepo(DUMP)

# inside the repo