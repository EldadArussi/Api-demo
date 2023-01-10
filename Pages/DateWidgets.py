from selenium.webdriver.common.by import By
from Infra.BasePage import BasePage


class DateWidgets(BasePage):
    dialog_btn = (By.XPATH, "//*[@content-desc='1. Dialog']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_dialog(self):
        self.click_on_element(self.dialog_btn)
