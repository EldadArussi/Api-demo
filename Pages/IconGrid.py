from selenium.webdriver.common.by import By
from Infra.BasePage import BasePage


class IconGrid(BasePage):
    list_icon_grid = (By.CLASS_NAME, "android.widget.ImageView")

    def __init__(self, driver):
        super().__init__(driver)

    def get_count_icon_grid(self):
        return self.get_count_of_elements(self.list_icon_grid)




