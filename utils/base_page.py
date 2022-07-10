from selenium.webdriver.support import expected_conditions as expected_conditions_module
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from driver.driver_chrome import driver
from selenium.webdriver.common.action_chains import ActionChains


def wait_for_element_by_condition(locator, expected_condition, value=None):
    """
    Espera hasta que el WebElement se encuentre en la condición solicitada

    :param expected_condition: La condición por la que se quiere esperar
    :param locator: La tupla que identifica al elemento (By.ID, id_del_elemento)
    :param value: Valor extra que necesite la expected condition
    :return: None
    """
    if not hasattr(expected_conditions_module, expected_condition.__name__):
        raise ValueError('INVALID CONDITION!: Must be an ExpectedCondition from Selenium library.')
    print(f'Wait for element: {locator} by condition: {expected_condition.__name__}')

   
    
    if value:
        return WebDriverWait(driver,10).until(expected_condition(locator,value))
    else:
        element = WebDriverWait(driver,10).until(expected_condition(locator))
        print(element,"element")
        return element

def hover_and_click(locator):
    # No es necesario utilizar "wait for element"
    element = driver.find_element(*locator)
    ActionChains(driver).move_to_element(element).click().perform()