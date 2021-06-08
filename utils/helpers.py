from pages.BaseApp import MainPage
from locators.locators import Locators
from selenium.webdriver.common.keys import Keys


class Helper(MainPage):

    def check_currency(self):
        return self.find_element(Locators.LOCATOR_CURRENCY, time=2).text

    def check_currency_in_price(self):
        return self.find_elements(Locators.LOCATOR_PRICE, time=2)

    def select_currency(self):
        return self.find_element(Locators.LOCATOR_CURRENCY_SELECTION, time=5).click()

    def dollar_currency(self):
        return self.click_element(Locators.LOCATOR_CURRENCY_DOLLAR, time=5).click()

    def select_dress(self):
        select_dress = self.find_element(Locators.LOCATOR_FOUND, time=2)
        return select_dress.clear, select_dress.send_keys('dress', Keys.ENTER)

    def check_text_num_product(self):
        return self.find_element(Locators.LOCATOR_NUMBER_PRODUCTS_TEXT, time=2).text

    def check_num_product(self):
        return self.find_elements(Locators.LOCATOR_NUMBER_PRODUCTS, time=2)

    def check_price_in_dollar(self):
        return self.find_elements(Locators.LOCATOR_PRICE, time=2)

    def click_sorting(self):
        return self.click_element(Locators.LOCATOR_SELECT_TITLE, time=2).click()

    def sorting_from_high(self):
        return self.click_element(Locators.LOCATOR_SORTING_FROM_HIGH, time=2).click()

    def check_sorting(self):
        return self.find_elements(Locators.LOCATOR_PRICE_FROM_HIGH, time=2)

    def product(self):
        return self.find_elements(Locators.LOCATOR_PRODUCT, time=2)

    def discount_product(self):
        return self.find_elements(Locators.LOCATOR_DISCOUNT_PRODUCT, time=2)

    def regular_price(self):
        return self.find_elements(Locators.LOCATOR_REGULAR_PRICE, time=2)

    def discount_percentage(self):
        return self.find_elements(Locators.LOCATOR_DISCOUNT_PERCENTAGE, time=2)

    def price_in_discount(self):
        return self.find_elements(Locators.LOCATOR_PRICE_IN_DISCOUNT, time=2)
