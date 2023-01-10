from selenium.webdriver.common.by import By
from Infra.UtilActions import UtilActions
from Infra.BasePage import BasePage


class LightTheme(BasePage):
    input_field = (By.ID, "io.appium.android.apis:id/edit")
    check_box_2 = (By.ID, "io.appium.android.apis:id/check2")
    radio_btn_2 = (By.ID, "io.appium.android.apis:id/radio2")
    drop_down = (By.ID, "io.appium.android.apis:id/spinner1")
    save_btn = (By.ID, "io.appium.android.apis:id/button")
    jupiter_planet = (By.XPATH, "//*[@text = 'Jupiter']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_input_field(self, text):
        self.click_on_element(self.input_field)
        self.fill_text(self.input_field, text)

    def check_check_box_2(self):
        self.click_on_element(self.check_box_2)

    def select_radio_btn(self):
        self.click_on_element(self.radio_btn_2)

    def select_jupiter_planet(self):
        UtilActions.scroll_by_coordinates(start_x=150, start_y=400, end_x=150, end_y=100)
        self.click_on_element(self.drop_down)
        self.click_on_element(self.jupiter_planet)

    def click_on_save(self):
        UtilActions.scroll_by_coordinates(start_x=150, start_y=400, end_x=150, end_y=1000)
        self.click_on_element(self.save_btn)
