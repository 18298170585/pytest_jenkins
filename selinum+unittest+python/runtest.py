# coding=utf-8
import unittest
import time

import os

from test_case.test_baidu import BaiduTest
from test_case.test_youdao import YoudaoTest
import HTMLTestRunner

# 构造测试集
suite=unittest.TestSuite()
suite.addTest(BaiduTest('test_baidu'))
suite.addTest(YoudaoTest('test_youdao'))

if __name__ == '__main__':
    # 执行测试的用例类
    dir = os.getcwd()
    outfile = open(dir + "/Phototests.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='测试报告', description='测试报告详情')
    runner.run(suite)

    # runner=unittest.TextTestRunner()
    # runner = HTMLTestRunner.HTMLTestRunner()
    # runner.run(suite)