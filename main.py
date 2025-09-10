import time
import undetected_chromedriver as UC

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from cookie_clicker import CookieClicker
from item_shop import ItemShop

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

driver = UC.Chrome(options=chrome_options, version_main=139)

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)

# Accept cookies if banner appears
try:
    cookie_banner = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cc_container--open a"))
    )
    cookie_banner.click()
except:
    print("No cookie banner found")

# Select English
language_selector = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div#langSelect-EN"))
)
language_selector.click()

# Main clicking loop
counter = 0
purchase_interval = 50  # Every 50 clicks, we try to purchase a product
item_shop = ItemShop(driver)


while True:
    CookieClicker.click_cookie(driver)
    counter += 1

    if counter >= purchase_interval:
        # Check the number of cookies before trying to buy
        cookie_num = item_shop.get_cookie_num()
        print(f"Cookies available: {cookie_num}")

        # Attempt to purchase the most expensive product you can afford
        item_shop.purchase_product()

        # Reset the counter after purchase
        counter = 0

    time.sleep(0.1)
