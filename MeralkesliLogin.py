from selenium import webdriver
from selenium.webdriver.common.by import By
import time




class LogIn():
    baseUrl = "https://www.phptravels.net"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(3)

    def test1(self):
        ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]").click()
        ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Login')]").click()
        ff.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("summer2019@gmail.com")
        ff.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("2019Summer")
        ff.driver.find_element_by_xpath("//input[@id='remember-me']").click()
        ff.driver.find_element_by_xpath("//button[@class='btn btn-action btn-lg btn-block loginbtn']").click()

    # def test2(self):
    #     ff.driver.find_element_by_xpath("//a[@class='btn btn-default br25 btn-block']").click()
    #
    # def test3(self):
    #     ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]").click()
    #     ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Login')]").click()
    #     ff.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("summer209@gmail.com")
    #     ff.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("2019Summer")
    #     ff.driver.find_element_by_xpath("//input[@id='remember-me']").click()
    #     ff.driver.find_element_by_xpath("//button[@class='btn btn-action btn-lg btn-block loginbtn']").click()
    #
    # def test4(self):
    #     ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]").click()
    #     ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Login')]").click()
    #     ff.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("summer2019gmail.com")
    #     ff.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("2019Summer")
    #     ff.driver.find_element_by_xpath("//input[@id='remember-me']").click()
    #     ff.driver.find_element_by_xpath("//button[@class='btn btn-action btn-lg btn-block loginbtn']").click()
    #
    # def test5(self):
    #     ff.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]").click()
    #     ff.driver.find_element_by_xpath( "//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Login')]").click()
    #     ff.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("summer2019@gmail.com")
    #     ff.driver.find_element_by_xpath("//input[@id='remember-me']").click()
    #     ff.driver.find_element_by_xpath("//button[@class='btn btn-action btn-lg btn-block loginbtn']").click()
    #

ff = LogIn()
ff.test1()
# ff.test2()
# ff.test3()
# ff.test4()
# ff.test5()