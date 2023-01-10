from selenium.webdriver.common.by import By
from Infra.BasePage import BasePage


class Controls(BasePage):
    light_theme = (By.XPATH, "//*[@content-desc='1. Light Theme']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_light_theme(self):
        self.click_on_element(self.light_theme)




