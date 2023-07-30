import pytest
from PageObjects.HomePage import HomePage
from PageObjects.SearchPage import SearchPage
from Tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class TestSearch(BaseTest):
    @pytest.mark.parametrize("product_name", ExcelUtils.get_data_from_excel("TestData/LambdaTest.xlsx", "Products"))
    def test_search_valid_item(self, product_name):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box(product_name)
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_hp_product()
