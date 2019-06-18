from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Recovery():
    def test1(self):
        baseUrl = "https://www.phptravels.net"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a").click()
        driver.find_element_by_xpath("/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[2]/ul[1]/li[1]/ul[1]/li[1]/a[1]").click()
        driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("durumehmet@gmail.com")
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("5C0HayPd")
        driver.execute_script("window.scrollBy(0,1000);")
        driver.find_element_by_xpath("//a[@class='btn btn-default br25 btn-block']").send_keys("5C0HayPd")
        driver.find_element_by_xpath("//a[@class='btn btn-default br25 btn-block']").click()
        driver.find_element_by_xpath("//input[@id='resetemail']").send_keys("durumehmet@gmail.com")
        driver.find_element_by_xpath("//button[@class='btn btn-primary resetbtn']").click()

        baseUrl = "https://www.google.com/gmail/about/"
        driver.get(baseUrl)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[4]/ul[1]/li[2]/a[1]").click()
        time.sleep(2)
        driver.find_elements_by_xpath("//input[@id='identifierId']").send_keys("durumehmet@gmail.com")



ff = Recovery()
ff.test1()
