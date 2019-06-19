from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class TC001 ():
    def sign_up_test(self):
        baseUrl = "https://www.phptravels.net/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


        my_account = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)

        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys("Emily")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Johnson")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnson@gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)
#
        sign_up_click = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)




ff = TC001()
ff.sign_up_test()


class TC002():
    def invalid_test(self):
        baseUrl = "https://www.phptravels.net/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        my_account = driver.find_element_by_xpath( "//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)

        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys("Emily")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Johnson")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnson2gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)

        sign_up_click = driver.find_element_by_xpath(" //button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)

        message = driver.find_element_by_xpath("//p[contains(text(),'The Email field must contain a valid email address')] ")
        print(message.text)

ff = TC002()
ff.invalid_test()


class TC003():
    def blank_name(self):
        baseUrl = "https://www.phptravels.net/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        my_account = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)



        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys(" ")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Johnson")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnson@gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)

        sign_up_click = driver.find_element_by_xpath(" //button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(3)

        message1 = driver.find_element_by_css_selector("section.login:nth-child(3) div.container div.row div.col-md-6.col-md-offset-3.col-sm-6.col-sm-offset-3 div.panel.panel-default div.panel-body div:nth-child(1) form:nth-child(1) div.resultsignup:nth-child(2) div.alert.alert-danger > p:nth-child(1)")
        print(message1.text)

ff = TC003()
ff.blank_name()

class TC004():
    def blank_last_name(self):
        baseUrl = "https://www.phptravels.net/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        my_account = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)

        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys("Emily ")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys(" ")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnson@gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)

        sign_up_click = driver.find_element_by_xpath(" //button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(3)

        message2 = driver.find_element_by_xpath("//p[contains(text(),'The Last Name field is required.')] ")
        print(message2.text)


ff = TC004()
ff.blank_last_name()


class TC010():
    def invalid_confirm_password(self):
        baseUrl = "https://www.phptravels.net/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        my_account = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)

        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys("Emily ")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Johnson")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnson@gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJrose80")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)

        sign_up_click = driver.find_element_by_xpath(" //button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(3)

        message3 = driver.find_element_by_css_selector(" section.login:nth-child(3) div.container div.row div.col-md-6.col-md-offset-3.col-sm-6.col-sm-offset-3 div.panel.panel-default div.panel-body div:nth-child(1) form:nth-child(1) div.resultsignup:nth-child(2) div.alert.alert-danger > p:nth-child(1)")
        print(message3.text)


ff = TC010()
ff.invalid_confirm_password()


class TC011():
    def used_email(self):
        baseUrl = ("https://www.phptravels.net/")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


        my_account = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)

        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys("Emily")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Johnson")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnson@gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)

        sign_up_click = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(3)

        message4 = driver.find_element_by_css_selector("section.login:nth-child(3) div.container div.row div.col-md-6.col-md-offset-3.col-sm-6.col-sm-offset-3 div.panel.panel-default div.panel-body div:nth-child(1) form:nth-child(1) div.resultsignup:nth-child(2) > div.alert.alert-danger")
        print(message4.text)


ff = TC011()
ff.used_email()


class TC014():
    def all_fill_out(self):

        baseUrl = "https://www.phptravels.net/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


        my_account = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')] ")
        my_account.click()
        time.sleep(3)

        sign_up = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//ul[@class='nav navbar-nav navbar-side navbar-right sidebar go-left user_menu']//li[@id='li_myaccount']//ul[@class='dropdown-menu']//li//a[@class='go-text-right'][contains(text(),'Sign Up')] ")
        sign_up.click()
        time.sleep(3)

        name = driver.find_element_by_xpath("//input[@placeholder='First Name'] ").send_keys("Emily")
        time.sleep(3)

        last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Johnson")
        time.sleep(3)

        phone_number = driver.find_element_by_xpath("//input[@placeholder='Mobile Number'] ").send_keys("857-412-7123")
        time.sleep(3)

        email = driver.find_element_by_xpath("//input[@placeholder='Email'] ").send_keys("rosemily.johnso@gmail.com")
        time.sleep(3)

        password = driver.find_element_by_xpath("//input[@placeholder='Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        confirm_password = driver.find_element_by_xpath("//input[@placeholder='Confirm Password'] ").send_keys("EJ80rose")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,150);")
        time.sleep(3)
    #
        sign_up_click = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg'] ")
        sign_up_click.click()
        time.sleep(3)

        #print("Sign up successfully")




ff = TC014()
ff.all_fill_out()











