from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_icon2(self):
        try:
            self.find_element(locator="username")
        except NoSuchElementException:
            return False
        return True
    def exist_icon3(self):
        try:
            self.find_element(locator="password")
        except NoSuchElementException:
            return False
        return True