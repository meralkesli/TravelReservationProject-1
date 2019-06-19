package com.cambridge.qa.testcases;

import java.io.FileNotFoundException;

import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import com.cambridge.qa.base.TestBase;
import com.cambridge.qa.pages.AboutPage;

import junit.framework.Assert;

public class AboutPageTest extends TestBase {

	AboutPage aboutPage;

	public AboutPageTest() throws FileNotFoundException {
		super();
// super class constructor will initialize the method below
	}

	@BeforeTest
	public void SetUp() throws FileNotFoundException {
		initilization();
		aboutPage = new AboutPage();
	}

	@Test(priority=1)
	public void clickAboutUsTest() {
		aboutPage.clickAboutUs();

	}

	@Test(priority=2)
	public void validateAboutUsPageTitleTest() {
		String title = aboutPage.validateAboutUsPageTitle();
		Assert.assertEquals(title, "About Us – Cambridge Consulting Group");
	}

	@Test(priority=3)
	public void validateCCLogoTest() {
		boolean logo = aboutPage.validateCCLogo();
		Assert.assertTrue(logo);
	}
	
	@Test(priority=4)
	public void clickWhoWeAreTest() {
		aboutPage.clickWhoWeAre();
	}
	
	@Test(priority=5)
	public void clickWhatWeDoTest() {
		aboutPage.clickWhatWeDo();
	}
	
	@Test(priority=6)
	public void clickOurMissionTest() {
		aboutPage.clickOurMission();
	}
	
	@Test(priority=7)
	public void clickOurVisionTest() {
		aboutPage.clickOurVision();
	}

	@AfterTest
	public void tearDown() {
		driver.quit();
	}
}
