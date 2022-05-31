from selenium import webdriver
from niked.sizes import get_sizes_skus
from niked.check_size import check_size
from niked.support import wait_for_load


url = input('Enter shoes url: ')
driver = webdriver.Safari()
driver.get(url)
wait_for_load(driver)

# get all sizes and print them
sizes_skus = get_sizes_skus(driver)
print('All sizes: ', list(sizes_skus.keys()))

user_size = input('Pick size: ')

# get unique sku for the size and check if available
user_size_sku = sizes_skus[user_size]
result = check_size(driver, user_size_sku)

print(result)

driver.quit()