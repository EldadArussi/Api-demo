from appium.webdriver.common.touch_action import TouchAction
from Infra.BaseTest import BaseTest


class UtilActions:
    @classmethod
    # This function scrolls by coordinates
    def scroll_by_coordinates(cls,start_x, start_y, end_x, end_y):
        action = TouchAction(BaseTest.get_driver())
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()