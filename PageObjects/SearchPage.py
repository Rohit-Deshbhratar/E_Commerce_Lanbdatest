from PageObjects.BaseClass import BaseClass


class SearchPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"

    def display_status_of_hp_product(self):
        return self.check_display_status_of_element("valid_hp_product_link_text", self.valid_hp_product_link_text)
