import pytest
from page_objects.login_page import LoginPage
from page_objects.shop_page import ShopPage


class TestLogin:
    @pytest.mark.login
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_browser()
        login_page.login_action("admin@onet.pl", "Adminadmin1!")

    @pytest.mark.parametrize("username,password",
                             [('admin2@onet.pl', 'Adminadmin1!'),
                              ('admin2@onet.pl', 'Adminadmin1!')])
    def test_check_cart_total_price(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open_browser()
        login_page.login_action(username, password)
        shopping_page = ShopPage(driver)
        shopping_page._check_total_price()

    @pytest.mark.parametrize("category,item,quantity",
                             [('Tops', 'Little Black Shirt', 1),
                              ('Scarfs', 'Andora Scarf', 1)])
    def test_add_products_to_cart(self, driver, category, item, quantity):
        login_page = LoginPage(driver)
        login_page.open_browser()
        shopping_page = ShopPage(driver)
        current_item, current_price, current_quantity = shopping_page._add_item_to_cart(category, item, quantity)
        shopping_page._check_item_in_cart(current_item, current_price, current_quantity)