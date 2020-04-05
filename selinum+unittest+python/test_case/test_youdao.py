# coding=utf-8
from selenium import webdriver
import unittest,time


class YoudaoTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="http://www.youdao.com"

    def test_youdao(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u'你好')
        driver.find_element_by_id("translateContent").submit()
        time.sleep(5)
        page_soure=driver.page_source
        self.assertIn('hello',page_soure)

    def tearDown(self):
        self.driver.quit()
        print('test is over')


if __name__ == '__main__':
    # 1
    unittest.main()
    # 2
    # suite=unittest.TestSuite()
    # suite.addTest(YoudaoTest('test_youdao'))
    # runer=unittest.TextTestRunner()
    # runer.run()