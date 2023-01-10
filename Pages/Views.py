from selenium.webdriver.common.by import By
from Infra.BasePage import BasePage


class Views(BasePage):
    data_widgets_btn = (By.XPATH, "//*[@content-desc='Date Widgets']")
    grid_btn = (By.XPATH, "	//*[@content-desc='Grid']")
    controls_btn = (By.XPATH, "	//*[@content-desc='Controls']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_data_widgets(self):
        self.click_on_element(self.data_widgets_btn)

    def click_on_grid(self):
        self.click_on_element(self.grid_btn)

    def click_on_controls(self):
        self.click_on_element(self.controls_btn)
