# -*- coding: UTF-8 -*-
import unittest
from time import sleep
from unittest.test.test_case import Test

from selenium.webdriver import Chrome, Ie, Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

# drive=Chrome()
# dr = Chrome()
# dr.get('http://www.python.org')
# sleep(5)
# # assert "Python" in dr.title
# elem = dr.find_element_by_name("q")
# elem.clear()
# elem.send_keys('pycon')
# # 键盘的输入
# elem.send_keys(Keys.RETURN)
# dr.close()  # 关闭当前窗口，如果是当前打开的最后一个窗口，则退出浏览器
# dr.quit()   # 退出驱动，关闭所有相关的窗口


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.drive = Chrome()

    @unittest.skipIf(True, '跳过一')
    def test2(self):
        print('test2')
        dr = self.drive
        dr.get("http://www.python.org")
        self.assertIn("Python", dr.title)
        elem = dr.find_element_by_name("q")
        elem.clear()
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in dr.page_source

    # @unittest.skip("用户名密码都为空用例不执行")
    # @unittest.skip(reason)：强制跳转。reason是跳转原因
    # @unittest.skipIf(condition, reason)：condition为True的时候跳转
    # @unittest.skipUnless(condition, reason)：condition为False的时候跳转
    # @unittest.expectedFailure：如果test失败了，这个test不计入失败的case数目
    def test1(self):
        print('test1')
        dr = self.drive
        dr.get("http://www.baidu.com/")
        self.assertIn ("百度一下，你就知道", dr.title)
        elem = dr.find_element_by_id("kw")
        elem.clear()
        elem.send_keys('py')
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in dr.page_source

    def tearDown(self):
        self.drive.close()


if __name__ == '__main__':
    # 执行的顺序是09，AZ，a~z
    # 1
    # unittest.main()
    # 2 实例化测试套件
    suite = unittest.TestSuite()
    suite.addTest(PythonOrgSearch('test2'))
    suite.addTest(PythonOrgSearch('test1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)