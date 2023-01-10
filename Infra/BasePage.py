class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    def fill_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_count_of_elements(self, locator):
        return len(self.driver.find_elements(by=locator[0], value=locator[1]))
