package com.cambridge.qa.util;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.apache.poi.EncryptedDocumentException;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

import com.cambridge.qa.base.TestBase;

public class TestUtil extends TestBase {

	public TestUtil() throws FileNotFoundException {
		super();
		// TODO Auto-generated constructor stub
	}

	public static int PAGE_LOAD_TIMEOUT = 20;
	public static int IMPLICIT_WAIT = 10;

	// you need to write common methods for any classes, like screenshot method or
	// change frame method

	public static Workbook book;
	public static Sheet sheet;

	public void switchToFrame() {
		driver.switchTo().frame("frame name");
		// to use this method in other classes, in other class you need to create first
		// object of this class
		// like TestUtil testUtil;
		// Then, in initialization method you will write testUtil = new TestUtil();
	}

	// Data import icin

	public static Object[][] getTestData(String sheetName) {
		FileInputStream file = null;

		try {
			// you add TESTDATA_SHEET_PATH
			file = new FileInputStream(
					"C:\\CODISTAN\\CambridgeConsultingTest\\src\\main\\java\\com\\cambridge\\qa\\testdata\\CambridgeConsultingTestData.xlsx");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			book = WorkbookFactory.create(file);
		} catch (EncryptedDocumentException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InvalidFormatException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		sheet = book.getSheet(sheetName);
		Object[][] data = new Object[sheet.getLastRowNum()][sheet.getRow(0).getLastCellNum()];
		System.out.println(sheet.getLastRowNum());

		System.out.println(sheet.getRow(0).getLastCellNum());
		for (int i = 0; i < sheet.getLastRowNum(); i++) {
			for (int j = 0; j < sheet.getRow(0).getLastCellNum(); j++) {

				data[i][j] = sheet.getRow(i + 1).getCell(j).toString();
				// System.out.println(data[i][j]);
			}
		}
		return data;

	}
	
	public static void takeScreenshotAtTheEnd() throws IOException{
		File srcfile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
		String currentDir = "C:\\CODISTAN\\CambridgeConsultingTest";
		FileUtils.copyFile(srcfile, new File(currentDir + "\\screenshots" + System.currentTimeMillis()+".png"));
	}
}
