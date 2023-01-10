import pytest
from appium import webdriver


class BaseTest:
    @pytest.fixture(scope='class')
    def init_app(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '9.0', 'deviceName': 'SM-G955F',
                        'appPackage': 'io.appium.android.apis', 'appActivity': 'io.appium.android.apis.ApiDemos'}

        BaseTest.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        BaseTest.driver.implicitly_wait(5)

        # Yield control to the test
        yield BaseTest.driver

        # Close the app after the test
        BaseTest.driver.quit()

    @classmethod
    def get_driver(cls):
        return cls.driver