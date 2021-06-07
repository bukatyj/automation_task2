from pages.BaseApp import MainPage
from locators.locators import Locators
from selenium.webdriver.common.keys import Keys


class Helper(MainPage):
    def check_current_price(self):
        currency = self.find_element(Locators.LOCATOR_CURRENCY, time=2).text
        currency_in_price = self.find_elements(Locators.LOCATOR_PRICE, time=2)
        return currency, currency_in_price

    def select_currency(self):
        return self.find_element(Locators.LOCATOR_CURRENCY_SELECTION, time=5).click()

    def dollar_currency(self):
        return self.click_element(Locators.LOCATOR_CURRENCY_DOLLAR, time=5).click()


    def select_dress(self):
        select_dress = self.find_element(Locators.LOCATOR_FOUND, time=2)
        return select_dress.clear, select_dress.send_keys('dress', Keys.ENTER)

    def check_num_product(self):
        text_num_product = self.find_element(Locators.LOCATOR_NUMBER_PRODUCTS_TEXT, time=2)
        num_product = self.find_elements(Locators.LOCATOR_NUMBER_PRODUCTS, time=2)
        return text_num_product, num_product

    def check_price_in_dollar(self):
        dollar_in_price = self.find_elements(Locators.LOCATOR_PRICE, time=2)
        return dollar_in_price

    def sorting_from_high(self):
        click_sorting = self.click_element(Locators.LOCATOR_SELECT_TITLE, time=5)
        sorting_from_high = self.click_element(Locators.LOCATOR_SORTING_FROM_HIGH, time=5)
        return click_sorting.click(), sorting_from_high.click()

    def check_sorting(self):
        sorting_price = self.find_elements(Locators.LOCATOR_PRICE_FROM_HIGH, time=2)
        return sorting_price