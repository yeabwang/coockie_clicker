from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CookieClicker:
    @staticmethod
    def click_cookie(driver):
        try:
            cookie = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "bigCookie"))
            )
            cookie.click()
        except Exception as e:
            print(f"Failed to click cookie: {e}")

