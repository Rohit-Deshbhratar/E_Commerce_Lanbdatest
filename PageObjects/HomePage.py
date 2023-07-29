from PageObjects.BaseClass import BaseClass
from PageObjects.SearchPage import SearchPage


class HomePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_xpath = "//input[@name='search']"
    search_button_xpath = "//button[contains(@class, 'btn-default')]"

    def enter_product_into_search_box(self, product_name):
        self.type_into_element(product_name, "search_box_field_xpath", self.search_box_field_xpath)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
