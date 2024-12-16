from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.common_ops import driver


class UiActions:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def wait_for_page_load(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            raise TimeoutException("The page did not load completely within the timeout period.")

    def fill_action(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def click_action(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()
        self.wait_for_page_load()

    def drop_down_select(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.send_keys(text)

    def is_element_visible(self, locator):
        self.wait_for_page_load()
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        self.wait_for_page_load()
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
