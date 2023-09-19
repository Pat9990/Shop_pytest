from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver

class LoginPage(BasePage):
    __url = "https://skleptest.pl/"
    __username = "admin@onet.pl"
    __password = "Adminadmin1!"
    __account_btn = (By.XPATH, "//li[@class='top-account']//a")
    __login_btn = (By.XPATH,"//input[@type='submit']")
    __username_field = (By.XPATH,"//input[@id='username']")
    __password_field = (By.XPATH,"//input[@id='password']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_browser(self):
        super()._open_url(self.__url)

    def login_action(self, username: str, password :str):
        super()._click(self.__account_btn)
        super()._input(self.__username_field,username)
        super()._input(self.__password_field, password)
        super()._click(self.__login_btn)