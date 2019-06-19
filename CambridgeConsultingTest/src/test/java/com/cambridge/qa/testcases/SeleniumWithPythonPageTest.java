package com.cambridge.qa.testcases;

import java.io.FileNotFoundException;

import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import com.cambridge.qa.base.TestBase;
import com.cambridge.qa.pages.SeleniumWithPythonPage;
import com.cambridge.qa.pages.ServicesPage;
import com.cambridge.qa.util.TestUtil;

public class SeleniumWithPythonPageTest extends TestBase {

	ServicesPage servicesPage;
	SeleniumWithPythonPage seleniumWithPython;
	String sheetName = "Sheet1";

	public SeleniumWithPythonPageTest() throws FileNotFoundException {
		super();
		// constructor for parent class
	}

	@BeforeTest
	public void setUp() throws FileNotFoundException {
		initilization();

		servicesPage = new ServicesPage();
		servicesPage.moveMouseOnServices();
		seleniumWithPython = servicesPage.clickSeleniumWithPython();
	}

	@Test(priority = 1)
	public void verifySeleniumPageTitleTest() {
		String titleSeleniumPage = seleniumWithPython.getPageTitle();
		Assert.assertEquals(titleSeleniumPage, "SELENIUM WEBDRIVER WITH PYTHON – Cambridge Consulting Group");

	}

	@Test(priority = 2)
	public void enterYourNameTest() {
		seleniumWithPython.enterYourName();
	}

	@Test(priority = 3)
	public void enterYourNumberTest() {
		seleniumWithPython.enterYourNumber();
	}

	@Test(priority = 4)
	public void enterYourEmailTest() {
		seleniumWithPython.enterYourEmail();

	}

	@Test(priority = 5)
	public void enterYourMessageTest() {
		seleniumWithPython.enterMessage();
	}

	@Test(priority = 6)
	public void clickSendTest() {
		seleniumWithPython.enterSend();
	}

	@Test(priority = 7)
	public void clickCloseButtonTest() {
		seleniumWithPython.clickCloseButton();

	}
	
	@DataProvider
	public Object[][] getCambridgeConsultingTestData() {
		Object data[][] = TestUtil.getTestData(sheetName);
		return data;
	}
	
	@Test (priority=8, dataProvider="getCambridgeConsultingTestData")
	public void enterTestDataTest(String Name, String phoneNumber, String Email, String message ) {
		seleniumWithPython.enterTestData(Name, phoneNumber, Email, message);
		
	}

	@AfterTest
	public void tearDown() {
		driver.quit();
	}

}
