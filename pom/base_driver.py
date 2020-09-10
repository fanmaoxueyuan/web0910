import os
from  selenium import  webdriver
from selenium.webdriver import DesiredCapabilities


class BaseDriver:
    driver = None
    def __init__(self):
        if not BaseDriver.driver:
            # driverpath = os.path.join(os.path.dirname(__file__), '../drivers/chromedriver.exe')
            # self.driver = webdriver.Chrome(executable_path=driverpath)
            # 使用远程浏览器
            self.driver = webdriver.Remote('http://49.233.108.117:4444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.CHROME)

            BaseDriver.driver = self.driver

            self.driver.maximize_window()
            self.driver.get('http://49.233.108.117:3000/')

        self.driver = BaseDriver.driver


    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
        BaseDriver.driver = None