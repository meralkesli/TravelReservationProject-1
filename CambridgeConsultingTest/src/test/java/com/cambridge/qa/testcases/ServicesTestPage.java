package com.cambridge.qa.testcases;

import java.io.FileNotFoundException;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import com.cambridge.qa.base.TestBase;
import com.cambridge.qa.pages.ServicesPage;

public class ServicesTestPage extends TestBase {
	
	ServicesPage servicesPage;
	//we create object of ServicesPage for object repository and actions

	public ServicesTestPage() throws FileNotFoundException {
		super();
		// this constructor is to reach for parent class
	}
	
	@BeforeMethod
	public void setUp() throws FileNotFoundException {
		initilization();
		servicesPage = new ServicesPage();
		servicesPage.moveMouseOnServices();
	}
	
	@Test(priority=1)
	public void clickCollegeCounselingTest() {
		servicesPage.clickCollegeCounseling();
	}
	
	@Test(priority=2)
	public void clickCareerCounselingTest() {
		servicesPage.clickCareerCounseling();
	}
	
	@Test(priority=3)
	public void clickPersonalCoachingTest() {
		servicesPage.clickPersonalCoaching();
	}
	
	@Test(priority=4)
	public void clickTutoringTest() {
		servicesPage.clickTutoring();
	}
	
	@Test(priority=5)
	public void clickCAMPTest() {
		servicesPage.clickCAMP();
	}
	
	@Test(priority=6)
	public void clickSeleniumWithPythonTest() throws FileNotFoundException {
		servicesPage.clickSeleniumWithPython();
	}
	
	@AfterMethod
	public void tearDown() {
		driver.quit();
		}
}
