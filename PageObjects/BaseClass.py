from selenium.webdriver.common.by import By


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.endswith("_clas"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_partial_link_text"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif locator_name.endswith("_tag_name"):
            element = self.driver.find_element(By.TAG_NAME, locator_value)
        return element

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()
