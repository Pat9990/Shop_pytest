from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
import re

class ShopPage(BasePage):

    __cart_btn = (By.XPATH,"//li[@class='top-cart']//a")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _add_item_to_cart(self, catagory_name: str, item_name: str, quantity: int):
        add_to_cart_btn = (By.XPATH,f"//*[contains(text(),'{item_name}')]/ancestor::li//a[contains(text(),'Add to cart')]")
        item_price_field = (By.XPATH,f"//*[contains(text(),'{item_name}')]/ancestor::li//a//span//span[@class='woocommerce-Price-amount amount']")
        super()._go_to_subtab(catagory_name)
        super()._wait_until_page_contains(catagory_name)
        price = super()._find(item_price_field).text
        super()._wait_until_element_is_visible(add_to_cart_btn)
        for i in range(quantity):
            super()._click(add_to_cart_btn)
        return item_name, price, quantity

    def _check_item_in_cart(self, item_name: str, price: str, quantity: int):
        row_with_item = (By.XPATH,f"//a[contains(text(),'{item_name}')]/ancestor::tr")
        product_field = (By.XPATH,f"(//a[contains(text(),'{item_name}')]/ancestor::tr//td)[3]")
        price_field = (By.XPATH, f"(//a[contains(text(),'{item_name}')]/ancestor::tr//td)[4]")
        quantity_field = (By.XPATH, f"(//a[contains(text(),'{item_name}')]/ancestor::tr//td)[5]//input")
        super()._click(self.__cart_btn)
        try:
            super()._wait_until_element_is_visible(row_with_item)
        except:
            super()._reload_page()

        super()._wait_until_element_is_visible(row_with_item)
        item_name_text = super()._find(product_field).text
        price_text = super()._find(price_field).text
        quantity_text = super()._find(quantity_field).get_attribute('value')

        assert item_name == item_name_text, "Wrong value"
        assert price == price_text, "Wrong value"
        assert quantity == int(quantity_text), f"Wrong value '{quantity}' is diffenrent than '{quantity_text}'"

    def _check_total_price(self, shipping_price=12):
        product_total_field = (By.XPATH,"//tr[@class='woocommerce-cart-form__cart-item cart_item']")
        cart_subtotal_field = (By.XPATH,"//th[contains(text(),'Subtotal')]//following-sibling::*//span")
        cart_total_field = (By.XPATH,"//th[contains(text(),'Total')]//following-sibling::*//span")
        subtotal_price = 0
        super()._click(self.__cart_btn)
        quantity_of_products = int(super()._get_element_count(product_total_field))

        for i in range(1, quantity_of_products+1):
            product_price_field = (By.XPATH, f"(//tr[@class='woocommerce-cart-form__cart-item cart_item'])[{i}]//td[6]//span")
            product_price = super()._get_text(product_price_field)
            product_price = re.findall("\d+", product_price)[0]
            subtotal_price = subtotal_price + int(product_price)

        cart_subtotal_price = re.findall("\d+",super()._get_text(cart_subtotal_field))[0]
        print(subtotal_price)
        print(cart_subtotal_price)
        assert int(cart_subtotal_price) == int(subtotal_price), "Wrong subtotal price"
        cart_total_price = re.findall("\d+",super()._get_text(cart_total_field))[0]
        assert int(cart_total_price) == (int(cart_subtotal_price)+shipping_price), "Wrong total price"

