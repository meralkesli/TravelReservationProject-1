from selenium import webdriver
import time


class Tc001():
    def test1(self):

        """Enter Valid mail address and password"""

        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        #Step-1 Navigate to www.phptravels.net
        myaccount = driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right hidden-sm go-left']//a[@class='dropdown-toggle go-text-right'][contains(text(),'My Account')]").click()
        time.sleep(2)

        #Step-2 Click MyAccount Button and SignIn
        signinbutton = driver.find_element_by_xpath("/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[2]/ul[1]/li[1]/ul[1]/li[2]/a[1]").click()
        time.sleep(3)

        #Step-3 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        #Step-4 Enter valid phone number
        phonenumber = driver.find_element_by_xpath("//input[@placeholder='Mobile Number']").send_keys("8571231212")

        time.sleep(2)
        #Step-5 Enter valid username
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        #Step-6 Enter valid password with 8 characters
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        #Step-7 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        #Step-8 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        print("Complete Sign In. Thank you Andersonnn..")

class Tc002():

    """Leave to empty eMail """

    def test2(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        #Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']")
        time.sleep(2)
        # Step-3 Enter valid password with 8 characters
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Email field is required.')]")
        print("As Expected; ", warningmessage.text)
class Tc003():

    """Leave to empty Password"""

    def test3(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Leave to empty Password
        password = driver.find_element_by_xpath("//input[@placeholder='Password']")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath(
            "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'The Password field is required.')]")
        print("As Expected; ", warningmessage.text)

class Tc004():

    """Password between 1-7 characters"""

    def test4(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter password 3 characters.
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("asd")
        time.sleep(2)

        # Step-4 Enter valid 3 characters confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("asd")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message

        expectedmessage = "Password should be contain at least 8 character"
        warningmessage = driver.find_element_by_xpath("/html[1]/body[1]/div[5]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/div[2]/div[1]/p[1]").text
        if expectedmessage==warningmessage:
            print("As expected Warning message is : ", expectedmessage)
        elif expectedmessage != warningmessage:
            print("Warning message is ; ", warningmessage.text)
        else:
            print("Unexpected Error..")


class Tc005():

    """Password contains at 4 capital letters  and 4 digit characters"""

    def test5(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Password contains at 4 capital letters  and 4 digit characters
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASDF1234")
        time.sleep(2)

        # Step-4 Enter valid confirm password
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASDF1234")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath(
            "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

class Tc007():
    """
    Try available username or mail address
    """

    def test7(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)


        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter password 3 characters.
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Enter valid 3 characters confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath("//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message "eMail already exist"

        expectedmessage = "Email Already Exists."
        warningmessage = driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
        if expectedmessage==warningmessage:
            print("As expected Warning message is : ", expectedmessage)
        elif expectedmessage != warningmessage:
            print("Warning message is ; ", warningmessage.text)
        else:
            print("Unexpected Error..")

class Tc009():
    """
    Empty Confirm Password
    """
    def test9(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter valid password
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Empty confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath(
            "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message

        expectedmessage = "confirm password required."
        warningmessage = driver.find_element_by_xpath("// p[contains(text(), 'The Password field is required.')]").text
        if expectedmessage == warningmessage:
            print("As expected Warning message is : ", expectedmessage)
        elif expectedmessage != warningmessage:
            print("Warning message is ; ", warningmessage.text)
        else:
            print("Unexpected Error..")

class Tc011():
    def test11(self):
        baseUrl = "https://www.phptravels.net/register"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Step-1 Enter valid First Name and Last Name
        firstname = driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Anderson")
        lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Talisca")

        time.sleep(2)

        # Step-2 Don't Enter e-mail address
        username = driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("asd@hotmail.com")
        time.sleep(2)
        # Step-3 Enter password 3 characters.
        password = driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("ASdf1234")
        time.sleep(2)

        # Step-4 Enter valid 3 characters confirm passwords.
        confirmpassword = driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys("ZXcv8900")
        time.sleep(2)

        # Step-5 Click Submit button and go to my account page
        submitbutton = driver.find_element_by_xpath(
            "//button[@class='signupbtn btn_full btn btn-action btn-block btn-lg']").click()
        time.sleep(2)

        # User will see warning message "eMail already exist"

        expectedmessage = "Password not matching with confirm password."
        warningmessage = driver.find_element_by_xpath("//p[contains(text(),'Password not matching with confirm password.')]").text
        if expectedmessage == warningmessage:
            print("As expected Warning message is : ", expectedmessage)
        elif expectedmessage != warningmessage:
            print("Warning message is ; ", warningmessage.text)
        else:
            print("Unexpected Error..")


Tc1 = Tc001()
Tc1.test1()

Tc2=Tc002()
Tc2.test2()

Tc3=Tc003()
Tc3.test3()

Tc4=Tc004()
Tc4.test4()

Tc5 = Tc005()
Tc5.test5()

Tc7 = Tc007()
Tc7.test7()

Tc9 = Tc009()
Tc9.test9()

