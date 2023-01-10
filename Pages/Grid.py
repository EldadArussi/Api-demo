from selenium.webdriver.common.by import By

from Infra.BasePage import BasePage


class Grid(BasePage):
    icon_grid = (By.XPATH, "//*[@content-desc='1. Icon Grid']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_icon_grid(self):
        self.click_on_element(self.icon_grid)