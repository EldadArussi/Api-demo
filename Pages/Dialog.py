from selenium.webdriver.common.by import By
from Infra.BasePage import BasePage


class Dialog(BasePage):
    change_date_btn = (By.ID, "io.appium.android.apis:id/pickDate")
    nextMonth = (By.ID, "android:id/next")
    day = (By.XPATH, "//*[@content-desc='01 פברואר 2023']")
    approveBtn = (By.ID, "android:id/button1")

    change_time_btn = (By.ID, "io.appium.android.apis:id/pickTime")
    hour = (By.XPATH, "//*[@content-desc='12']")
    min = (By.XPATH, "//*[@content-desc='0']")
    dateDisplay = (By.ID, "io.appium.android.apis:id/dateDisplay")




    def __init__(self, driver):
        super().__init__(driver)

    def change_date(self):
        self.click_on_element(self.change_date_btn)
        self.click_on_element(self.nextMonth)
        self.click_on_element(self.day)
        self.click_on_element(self.approveBtn)

    def change_time(self):
        self.click_on_element(self.change_time_btn )
        self.click_on_element(self.hour)
        self.click_on_element(self.min)
        self.click_on_element(self.approveBtn)

    def get_date_time(self):
        return self.get_text_of_element(self.dateDisplay)


