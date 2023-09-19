import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException

class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver=driver

    def _find(self, locator: tuple) -> WebElement:
       return self._driver.find_element(*locator)

    def _get_element_count(self, locator: tuple) -> WebElement:
        return len(self._driver.find_elements(*locator))

    def _get_text(self, locator: tuple) -> str:
        return self._driver.find_element(*locator).text

    def _wait_until_element_is_visible(self, locator: tuple, time = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _click(self, locator:tuple):
        self._wait_until_element_is_visible(locator,30)
        self._find(locator).click()

    def _input(self, locator: tuple, text: str):
        self._wait_until_element_is_visible(locator, 30)
        self._find(locator).send_keys(text)

    def _open_url(self, url: str):
        self._driver.get(url)

    def _go_to_tab(self, tab_name: str):
        tab_field = (By.XPATH, f"//ul[@id='desktop-menu']//li//a[@title='{tab_name}']")
        self._click(self.__tab_field)

    def _go_to_subtab(self, subtab_name:str):
        subtab_field = (By.XPATH, f"//ul[@id='desktop-menu']//li//a[@title='Catergries']/parent::li//ul//li//a[@title='{subtab_name}']")
        tab_field = (By.XPATH, f"//ul[@id='desktop-menu']//li//a[@title='Catergries']")
        a = ActionChains(self._driver)
        tab_locator = self._find(tab_field)
        a.move_to_element(tab_locator).perform()
        self._click(subtab_field)

    def _wait_until_page_contains(self, text:str):
        WebDriverWait(self._driver, 20).until(ec.text_to_be_present_in_element((By.ID, "page"), f'{text}'))

    def _reload_page(self,url='https://skleptest.pl/cart/'):
        self._driver.get(url)
        self._driver.refresh()
        time.sleep(6)

