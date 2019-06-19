package com.cambridge.qa.pages;

import java.io.FileNotFoundException;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import com.cambridge.qa.base.TestBase;

public class ServicesPage extends TestBase {

	@FindBy(xpath = "//li[@id='menu-item-11859']//span[@class='menu-text'][contains(text(),'SERVICES')]")
	WebElement services;

	@FindBy(xpath = "//li[@id='menu-item-11915']//span[contains(text(),'COLLEGE COUNSELING')]")
	WebElement collegeCounseling;

	@FindBy(xpath = "//li[@id='menu-item-11897']//span[contains(text(),'CAREER COUNSELING')]")
	WebElement careerCounseling;

	@FindBy(xpath = "//li[@id='menu-item-11919']//span[contains(text(),'PERSONAL COACHING')]")
	WebElement personalCoaching;

	@FindBy(xpath = "//li[@id='menu-item-11924']//span[contains(text(),'TUTORING')]")
	WebElement tutoring;

	@FindBy(xpath = "//li[@id='menu-item-11928']//span[contains(text(),'C.A.M.P.')]")
	WebElement camp;

	@FindBy(xpath = "//li[@id='menu-item-12311']//span[contains(text(),'SELENIUM WEBDRIVER WITH PYTHON')]")
	WebElement seleniumWithPython;

	
	
	// initialize the page objects

	public ServicesPage() throws FileNotFoundException {

		PageFactory.initElements(driver, this);
	}

	// Actions

	public void moveMouseOnServices() {
		Actions action = new Actions(driver);
		action.moveToElement(services).build().perform();
	}

	public void clickCollegeCounseling() {
		collegeCounseling.click();
	}

	public void clickCareerCounseling() {
		careerCounseling.click();
	}

	public void clickPersonalCoaching() {
		personalCoaching.click();
	}

	public void clickTutoring() {
		tutoring.click();
	}

	public void clickCAMP() {
		camp.click();
	}

	public SeleniumWithPythonPage clickSeleniumWithPython() throws FileNotFoundException {
		seleniumWithPython.click();
		return new SeleniumWithPythonPage();
	}

}
