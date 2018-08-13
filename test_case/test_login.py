# -*- coding:utf-8 -*-
#date:  2018/7/14
import unittest
from  page.page import CreateBugPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = CreateBugPage()
        cls.page.open('http://zbox.imdsx.cn/user-login.html')

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.page.quit()

    def test_login(self):
        self.page.send_username()
        self.page.send_passwd()
        self.page.login_click()
        self.assertTrue(self.page.check_login('test_login'))

        self.page.bug()
        self.page.createBug()

        self.page.select_module()
        self.page.os()
        self.page.browser()
        self.page.assignedTo()
        self.page.deadline()
        self.page.openBuild()
        self.page.title()
        # self.page.pri()
        self.page.mailto()
        self.page.setMailto()
        self.page.keywords()
        self.page.info()
        # self.page.save()



if __name__ == '__main__':
    unittest.main()




