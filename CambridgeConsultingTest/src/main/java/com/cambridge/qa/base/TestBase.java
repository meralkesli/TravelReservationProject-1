package com.cambridge.qa.base;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.events.EventFiringWebDriver;

import com.cambridge.qa.util.TestUtil;
import com.cambridge.qa.util.WebEventListener;

public class TestBase {

	public static WebDriver driver;
	public static Properties prop;
	public static EventFiringWebDriver e_driver;
	public static WebEventListener eventListener;

	// We need to create the constructor of the Class
	public TestBase() throws FileNotFoundException {

		prop = new Properties();
		try {
			FileInputStream ip = new FileInputStream(
					"C:\\CODISTAN\\CambridgeConsultingTest\\src\\main\\java\\com\\cambridge\\qa\\config\\config.properties");

			prop.load(ip);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();

		}
	}

	public static void initilization() throws FileNotFoundException {
		String browserName = prop.getProperty("browser");

		if (browserName.equals("chrome")) {
			System.setProperty("webdriver.chrome.driver",
					"C:\\CODISTAN\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe");

			driver = new ChromeDriver();
		} else if (browserName.equals("firefox")) {
			System.setProperty("webdriver.gecko.driver",
					"C:\\CODISTAN\\SeleniumDrivers\\geckodriver-v0.23.0-win64\\geckodriver.exe");

			driver = new FirefoxDriver();

		} else if (browserName.equals("IE")) {
			// code comes here
		}
		//Add WebDriver Fire event : to generate selenium action logs
		e_driver = new EventFiringWebDriver(driver);
		//Now create object of EventListenerHandler to register it with EventFiringWebDriver
		eventListener = new WebEventListener();
		e_driver.register(eventListener);
		driver = e_driver;
		
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		driver.manage().timeouts().pageLoadTimeout(TestUtil.PAGE_LOAD_TIMEOUT, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(TestUtil.IMPLICIT_WAIT, TimeUnit.SECONDS);
		
		driver.get(prop.getProperty("url"));
		
	}
}
