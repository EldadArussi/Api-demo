from selenium.webdriver.common.by import By
from Infra.BasePage import BasePage


class Lobby(BasePage):
    views_screen_btn = (By.XPATH, "//*[@content-desc='Views']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_views_screen(self):
        self.click_on_element(self.views_screen_btn)
