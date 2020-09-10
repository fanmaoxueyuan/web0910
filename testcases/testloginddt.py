from ddt import ddt,data,unpack,file_data
from testcases.basecase import BaseCase
import unittest

@ddt
class TestDDTLogin(BaseCase):

    @unittest.skip('SkipTest')
    @data(('','123456'),('test10','654321'),('test10',''))
    @unpack
    def test_login(self,username,passwd):
        lp = self.mp.go_to_login_page()
        lp.login_with_username(username,passwd)

    @unittest.skip('Skip')
    @file_data('../data/login_data.json')
    def test_login_data(self,username,passwd):
        lp = self.mp.go_to_login_page()
        lp.login_with_username(username, passwd)

    @file_data('../data/login_data.yaml')
    def test_login_yaml(self,username,passwd):
        lp = self.mp.go_to_login_page()
        lp.login_with_username(username, passwd)


