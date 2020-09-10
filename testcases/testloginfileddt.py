from ddt import ddt,data,unpack,file_data
from testcases.basecase import BaseCase
from tools.datahandler import FileHanlder

fl = FileHanlder()
test_data = fl.read_csv('data/login_data.csv')   # [['username', 'passwd'], ['zhangsan', "''"], ['zhangsan', '123456'], ["''", "''"]]
test_data.pop(0)  # [['zhangsan', "''"], ['zhangsan', '123456'], ["''", "''"]]
@ddt
class TestDDTLogin(BaseCase):

    # @data(('','123456'),('test10','654321'),('test10',''))
    @data(*test_data)
    @unpack
    def test_login(self,username,passwd):
        lp = self.mp.go_to_login_page()
        lp.login_with_username(username,passwd)