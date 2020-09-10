import unittest
from pom.main_page import MainPage
class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.mp = MainPage()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mp.quit_driver()

    def setUp(self) -> None:
        """
        每个测试用例执行之前的操作
        :return:
        """
        self.mp.driver.get('http://49.233.108.117:3000/')

    def tearDown(self) -> None:
        """
        每个用例执行之后的操作
        :return:
        """
        import os,time
        screenshots = os.path.join(os.path.dirname(__file__),'../screenshots')
        if not os.path.exists(screenshots):
            os.mkdir(screenshots)
        filename = time.strftime('%Y_%m_%d_%H_%M_%S')+'.png'
        png_file = os.path.join(screenshots,filename)
        self.mp.driver.save_screenshot(png_file)