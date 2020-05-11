from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"