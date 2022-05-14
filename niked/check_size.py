from selenium.webdriver.common.by import By

def check_size(driver, sku):
    element = driver.find_element(By.ID, sku)

    if element.get_attribute('disabled'):
        return 'Size not available'
    else:
        return 'Size available!'
    