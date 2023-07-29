from PageObjects.HomePage import HomePage
from PageObjects.SearchPage import SearchPage
from Tests.BaseTest import BaseTest


class TestSearch(BaseTest):
    def test_search_valid_item(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("HP")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_hp_product()
