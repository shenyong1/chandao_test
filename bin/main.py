
import unittest
from lib.path import WEBCASEPATH,REPORTPATH
from lib.HTMLTestRunner import HTMLTestRunner
from lib.tool import Tool
from lib.logger import logger

class main(object):
    def run(self):
        Tool().clear_picture()
        suit = unittest.TestSuite()
        cases = unittest.defaultTestLoader.discover(WEBCASEPATH)

        for case in cases:
            suit.addTest(case)

        f = open(REPORTPATH,'wb')

        runner = HTMLTestRunner(f,verbosity=1,title='UI测试报告',description='用例执行情况：')
        res = runner.run(suit)

        logger.info('共运行%s条，成功%s条，失败%s条'%(res.all_count,res.success_count,res.failure_count))

        f.flush()
        f.close()

if __name__ == '__main__':
    main().run()