from selenium.webdriver.common.by import By


def get_sizes_skus(driver):
    """
    Returns sizes and their individual SKUs for selected shoe
    """
    
    sizes_table = driver.find_element(By.CSS_SELECTOR,
                                      'div.mt2-sm.css-12whm6j')
    sizes_divs = sizes_table.find_elements(By.TAG_NAME, 'div')
    sizes_skus = {
        size.text: size.find_element(By.TAG_NAME, 'input').get_attribute('id')\
            for size in sizes_divs
        }
    return sizes_skus

