# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
# import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#     "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# )

# # Force UC to use ChromeDriver
# driver = uc.Chrome(options=chrome_options, version_main=139)

# url = "https://orteil.dashnet.org/cookieclicker/"
# driver.get(url)

# # Accept cookies if banner appears
# try:
#     cookie_banner = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".cc_container--open a"))
#     )
#     cookie_banner.click()
# except:
#     print("No cookie banner found")

# # Select English
# language_selector = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "div#langSelect-EN"))
# )
# language_selector.click()

# def click_cookie():
#     # Wait for the big cookie
#     cookie = WebDriverWait(driver, 60).until(
#         EC.element_to_be_clickable((By.ID, "bigCookie"))
#     )

#     cookie.click()

# import time

# # Function to get the current number of cookies
# def get_cookie_num():
#     cookie_num = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "div#cookies"))
#     )
#     return int(cookie_num.text.split()[0].replace(",", ""))  # Assuming text format is "X cookies"
# def purchase_product():
#     store = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located(
#             (By.CSS_SELECTOR, "div#products .product.enabled")
#         )
#     )

#     # List to store available products and their prices
#     available_products = []

#     for product in store:
#         try:
#             # Get the product name and price
#             product_name = product.find_element(By.CSS_SELECTOR, ".productName").text
#             price_str = product.find_element(By.CSS_SELECTOR, ".price").text
#             price = int(price_str.replace(",", ""))  # Convert the price to integer

#             # Only add products that are affordable
#             if price <= get_cookie_num():
#                 available_products.append((price, product))  # Store the product and price

#         except Exception as e:
#             print(f"Error parsing product: {e}")
#             continue

#     if available_products:
#         # Sort by price (descending) and select the most expensive product that you can afford
#         available_products.sort(reverse=True, key=lambda x: x[0])

#         # Get the most expensive affordable product
#         most_expensive_product = available_products[0][1]

#         print(f"Purchasing product: {most_expensive_product.find_element(By.CSS_SELECTOR, '.productName').text}")

#         # Click on the product to purchase it
#         most_expensive_product.click()
#         time.sleep(1)  # Pause for 1 second to prevent rapid clicks


# # Main clicking loop
# counter = 0
# purchase_interval = 50  # Every 50 clicks, we try to purchase a product

# while True:
#     click_cookie()  # Click the big cookie
#     counter += 1  # Increment the click counter

#     if counter >= purchase_interval:
#         # Check the number of cookies before trying to buy
#         cookie_num = get_cookie_num()
#         print(f"Cookies available: {cookie_num}")

#         # Attempt to purchase the most expensive product you can afford
#         purchase_product()

#         # Reset the counter after purchase
#         counter = 0

#     time.sleep(0.1)  # Optional: Add a small delay between iterations to avoid overloading the CPU
