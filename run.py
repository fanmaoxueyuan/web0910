import unittest

def create_suite():
    # 实例化测试套件
    testsuite = unittest.TestSuite()
    # 测试加载器
    testloader = unittest.TestLoader()
    # 使用discover 加载所有的用例
    tests = testloader.discover(start_dir='testcases',pattern='test*.py')
    # 将用例存放在测试套件
    testsuite.addTests(tests)
    return testsuite

if __name__ == '__main__':
    # 测试执行器
    runer = unittest.TextTestRunner(verbosity=2)
    suite = create_suite()
    # 运行测试套件
    runer.run(suite)