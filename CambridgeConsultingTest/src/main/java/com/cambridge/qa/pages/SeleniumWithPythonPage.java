package com.cambridge.qa.pages;

import java.io.FileNotFoundException;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import com.cambridge.qa.base.TestBase;

public class SeleniumWithPythonPage extends TestBase {

	@FindBy(xpath = "//input[@name='your-name']")
	@CacheLookup // this annotation for cache memory , it will put this element 'yourName' , and if you use it so many times,
	//instead of going to page and look for element, it will call from cache memory so it will be faster
	//However, if the page will get refreshed, DOM can be changed, then some elements migth be not disturbed, some still can be used.
	//So you can get StaleElementExeption
	WebElement yourName;

	@FindBy(xpath = "//input[@name='tel-695']")
	WebElement phoneNumber;

	@FindBy(xpath = "//input[@name='your-email']")
	WebElement email;

	@FindBy(xpath = "//textarea[@name='your-message']")
	WebElement message;

	@FindBy(xpath = "//input[@class='wpcf7-form-control wpcf7-submit']")
	WebElement sendKey;

	@FindBy(xpath = "//button[@class='close toggle-alert']")
	WebElement closeButton;

	public SeleniumWithPythonPage() throws FileNotFoundException {
		// initialize the page objects
		PageFactory.initElements(driver, this);
	}

	// Actions
	public String getPageTitle() {

		return driver.getTitle();

	}

	public void enterYourName() {
		yourName.sendKeys("Dilber Er");
	}

	public void enterYourNumber() {
		phoneNumber.sendKeys("3125327308");
	}

	public void enterYourEmail() {
		email.sendKeys("dilberer@gmail.com");
	}

	public void enterMessage() {
		message.sendKeys("Hello...");
	}

	public void enterSend() {
		sendKey.click();
	}

	public void clickCloseButton() {
		closeButton.click();

	}

	public SeleniumWithPythonPage clickCloseButtonTest() throws FileNotFoundException {
		closeButton.click();
		return new SeleniumWithPythonPage();
	}

	public void enterTestData(String YourName, String yourNumber, String yourEmail, String yourMessage) {
		yourName.sendKeys(YourName);
		phoneNumber.sendKeys(yourNumber);
		email.sendKeys(yourEmail);
		message.sendKeys(yourMessage);
		sendKey.click();
		closeButton.click();
		
	}
}
