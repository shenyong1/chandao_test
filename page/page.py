# -*- coding:utf-8 -*-
#date:  2018/7/14
from lib.pyse import Pyse
from selenium.webdriver.support.select import Select
class BasePage(object):
    def __init__(self):
        self.pyse = Pyse('chrome')

    def open(self,url):
        self.pyse.open(url)

    def close(self):
        self.pyse.close()

    def quit(self):
        self.pyse.quit()

class LoginPage(BasePage):
    def send_username(self):
        css = 'id=>account'
        self.pyse.type(css,'admin')
    def send_passwd(self):
        css = 'name=>password'
        self.pyse.type(css,'houyafan123')
    def login_click(self):
        css = 'id=>submit'
        self.pyse.click(css)
    def check_login(self,name):
        css = 'xpath=>//div[@id="userMenu"]/a'
        res = self.pyse.wait_and_save_exception(css,name)
        return res

class Menu(LoginPage):
    def bug(self):
        css='css=>[href="/bug/"]'
        self.pyse.click(css)

class BugList(Menu):
    def createBug(self):
        css='css=>[href^="/bug-create"]'
        self.pyse.click(css)

class CreateBugPage(BugList):
    #第一种两次点击
    def module(self):
        css = 'css=>#module_chosen'
        css1 = 'css=>[data-keys="/denglumokuai /dlmk"]'
        self.pyse.click(css)
        self.pyse.click(css1)

    def select_module(self):
        js = 'document.getElementById("module").style.display = "";'
        self.pyse.js(js)
        css = 'css=>#module'
        self.pyse.select_by_value(css,'3')

    def os(self):
        css = 'css=>#os'
        self.pyse.select_by_value(css,'windows')

    def browser(self):
        css = 'css=>#browser'
        self.pyse.select_by_value(css,'ie11')

    def assignedTo(self):
        js = 'document.getElementById("assignedTo").style.display = "";'
        self.pyse.js(js)
        css = 'css=>#assignedTo'
        self.pyse.select_by_value(css,'admin')

    def deadline(self):
        css = 'css=>#deadline'
        self.pyse.type(css,'2018-08-08')

    def openBuild(self):
        js = 'document.getElementById("openedBuild").style.display = "";'
        self.pyse.js(js)
        css = 'css=>#openedBuild'
        self.pyse.select_by_value(css,'3')

    def title(self):
        css = 'css=>#title'
        self.pyse.type(css,'xiaoqing002自动化创建bug')

    def pri(self):
        # js = 'document.getElementById("severity").style.display = "";'
        js = '$("#pri").fadeOut();'
        self.pyse.js(js)
        css = 'css=>#pri'
        self.pyse.select_by_value(css,'3')


    def mailto(self):
        js = 'document.getElementById("mailto").style.display = "";'
        self.pyse.js(js)
        css = 'css=>#mailto'
        self.pyse.select_by_value(css,'admin')

    def setMailto(self):
        js = 'document.querySelectorAll("select")[10].style.display = "";'
        self.pyse.js(js)
        css = '''css=>[onchange="setMailto('mailto', this.value)"]'''
        self.pyse.select_by_value(css,'1')

    def keywords(self):
        css = 'id=>keywords'
        self.pyse.type(css,'bugbug')

    def info(self):
        js = "document.getElementById('steps').innerText='<p>[步骤11]</p ><p>1.测试步骤</p ><p>[结果22]</p ><p>2.测试结果</p ><p>[期望33]</p ><p>3.测试期望</p >';"
        self.pyse.js(js)

    def save(self):
        css = 'css=>#submit'
        js = 'window.scrollTo(1000,1000)'
        self.pyse.js(js)
        self.pyse.click(css)





