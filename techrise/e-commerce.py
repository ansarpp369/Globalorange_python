from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


def next_page_available():
    next = driver.find_elements(By.XPATH, "//span[contains(string(), 'Next')]")
    if len(next) == 0:
        return False
    return True


def accept_cookie():
    elem = driver.find_elements(By.XPATH, "//button[contains(string(), 'Accept all')]")[0]
    elem.click()
    time.sleep(5)


def click_next():
    next_element = driver.find_elements(By.XPATH, "//a[.//span[text()='Next']]")
    if len(next_element) == 0:
        return
    next_element[0].click()


def site_found():
    ecommerce_url = driver.find_elements(By.XPATH, "//h3[contains(string(), 'E-commerce in the Netherlands - statistics & facts - Statista')]")
    if len(ecommerce_url) > 0:
        return True
    return False


driver = webdriver.Chrome()

# Open google.com and search "e-commerce"
driver.get("https://www.google.com/search?q=e-commerce")

# Accept cookie consent
accept_cookie()

page_num = 1
found_on_page = 0

# Check E-commerce in the netherlands-statistics & facts among the results
while next_page_available():
    if page_num > 10:
        break

    if site_found():
        found_on_page = page_num
        break
    else:
        page_num += 1
        click_next()

assert found_on_page != 0
assert found_on_page <= 10

# Return page number with title and page no
print("E-commerce in the Netherlands - statistics & facts found in page no", found_on_page)

driver.quit()
