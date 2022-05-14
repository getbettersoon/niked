from selenium import webdriver
from niked.sizes import get_sizes_skus
from niked.check_size import check_size
from niked.support import wait_for_load


url = input('Enter shoe url: ')
driver = webdriver.Safari()
try:
    driver.get(url)
except Exception as e:
    print("Unexpected ", e)
wait_for_load(driver)

sizes_skus = get_sizes_skus(driver)

print('All sizes: ', list(sizes_skus.keys()))

user_size = input('Pick size: ')
user_size_sku = sizes_skus[user_size]

result = check_size(driver, user_size_sku)

print(result)

driver.quit()