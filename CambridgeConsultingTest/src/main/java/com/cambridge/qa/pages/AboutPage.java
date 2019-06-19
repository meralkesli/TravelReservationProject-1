package com.cambridge.qa.pages;

import java.io.FileNotFoundException;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import com.cambridge.qa.base.TestBase;

public class AboutPage extends TestBase {

	// PageFactory -OR:Object Repository
	@FindBy(xpath = "//li[@id='menu-item-11861']//span[@class='menu-text'][contains(text(),'ABOUT US')]")
	WebElement aboutUs;

	@FindBy(xpath = " //div[contains(text(),'Who we are?')]")
	WebElement whoWeAre;

	@FindBy(xpath = "//div[contains(text(),'What we do?')]")
	WebElement whatWeDo;

	@FindBy(xpath = "//div[contains(text(),'Our mission')]")
	WebElement ourMission;

	@FindBy(xpath = "//div[contains(text(),'Our vision')]")
	WebElement ourVision;

	@FindBy(xpath = "//a[@class='fusion-logo-link']")
	WebElement ccLogo;
	
	

	// we will create constructor of AboutPage class so we can initialize the
	// PageObjects
	public AboutPage() throws FileNotFoundException {

		PageFactory.initElements(driver, this);
		// All the element we declare above will be initialized with this driver
		// this refers the current class object
	}

	// Actions
	public boolean validateCCLogo() {
		return ccLogo.isDisplayed();
	}

	public String validateAboutUsPageTitle() {

		return driver.getTitle();

	}

	public void clickAboutUs() {
		aboutUs.click();
	}

	public void clickWhoWeAre() {
		whoWeAre.click();
	}

	public void clickWhatWeDo() {
		whatWeDo.click();
	}

	public void clickOurMission() {
		ourMission.click();
	}
	
	public void clickOurVision() {
		
		ourVision.click();
	}
}
