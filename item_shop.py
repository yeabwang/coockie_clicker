import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ItemShop:

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_cookie_num(self):
        cookie_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#cookies"))
        )
        text = cookie_elem.text.split()[0].replace(",", "")

        # Handle million, billion, trillion
        multiplier = 1
        if "million" in text:
            multiplier = 1_000_000
        elif "billion" in text:
            multiplier = 1_000_000_000
        elif "trillion" in text:
            multiplier = 1_000_000_000_000
        elif "quadrillion" in text:
            multiplier = 1_000_000_000_000_000

        num = int("".join(filter(str.isdigit, text)))
        return num * multiplier

    def purchase_product(
        self,
    ):
        store = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "div#products .product.enabled")
            )
        )

        available_products = []

        for product in store:
            try:
                product_name = product.find_element(
                    By.CSS_SELECTOR, ".productName"
                ).text
                price_str = product.find_element(By.CSS_SELECTOR, ".price").text
                price = int(price_str.replace(",", ""))

                # Only add products that are affordable
                if price <= self.get_cookie_num():
                    available_products.append(
                        (price, product)
                    )  # Store the product and price

            except Exception as e:
                print(f"Error parsing product: {e}")
                continue

        if available_products:
            available_products.sort(reverse=True, key=lambda x: x[0])
            product_to_buy_name = (
                available_products[0][1]
                .find_element(By.CSS_SELECTOR, ".productName")
                .text
            )

            for product in self.driver.find_elements(
                By.CSS_SELECTOR, "div#products .product.enabled"
            )[::-1]:
                name = product.find_element(By.CSS_SELECTOR, ".productName").text
                if name == product_to_buy_name:
                    print(f"Purchasing product: {name}")
                    product.click()
                    time.sleep(1)
                    break
