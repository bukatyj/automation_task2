from utils.helpers import Helper
from time import sleep
import pytest


class Test:
    def test(self, browser):
        prestashop_page = Helper(browser)
        prestashop_page.go_to_site()

        sleep(5)
        prestashop_page.select_currency()
        sleep(5)
        prestashop_page.dollar_currency()

        prestashop_page.select_dress()


        prestashop_page.sorting_from_high()

def test():
    assert 2 == 2