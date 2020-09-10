import unittest
# 继承TestCase
from testcases.basecase import BaseCase

class TestLoginCase(BaseCase):

    def test_login_failed1(self):
        lp = self.mp.go_to_login_page()
        lp.login_with_username('zhangsan','123456')
        # 对登录结果进行验证
        fail_text = lp.login_fail_text()
        assert fail_text == "用户名或密码错误"

    def test_login_success(self):
        lp = self.mp.go_to_login_page()
        lp.login_with_username('test30','123456')
        # 对登录结果进行验证
        success_text = self.mp.user_logined_text()
        assert success_text == 'test30'

    def test_login_failed2(self):
        lp = self.mp.go_to_login_page()
        lp.login_with_username('','123456')
        # 对登录结果进行验证
        fail_text = lp.login_fail_text()
        assert fail_text == "信息不完整"

if __name__ == '__main__':
    unittest.main(verbosity=2)

