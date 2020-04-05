# coding=utf-8
from selenium import webdriver
import unittest ,time


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.drive=webdriver.Chrome()
        self.drive.implicitly_wait(30)
        self.base_url="https://www.baidu.com"

    def test_baidu(self):
        driver=self.drive
        driver.get(self.base_url+'/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        title=driver.title
        self.assertEqual(title,u"unittest_百度搜索")

    def tearDown(self):
        self.drive.quit()


if __name__ == '__main__':
    unittest.main()
    # 2实例化测试套件
    # suite=unittest.TestSuite()
    # # 添加测试的用例
    # suite.addTest(BaiduTest('test_baidu'))
    # # 实例化TextTestRunner类
    # runner=unittest.TextTestRunner()
    # # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    # runner.run(suite)