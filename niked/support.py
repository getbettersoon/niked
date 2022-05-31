from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_load(driver):
    """
    Waits until JavaScript portion of size table is rendered in browser
    """
    try:
        WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.ID, 'buyTools')))
    except Exception as e:
        print('Exception', e)
        driver.quit()