import pytest
from selenium import webdriver 
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils
import time
import datetime

#PROBLEM: THE "test_login_ddt" TEST CASE RUNS 4 DIFFERENT TEST CASE INSTANCES USING DIFFERENT DATA, BUT IT IS ALL CONSIDERED AS ONE.
#SHOULD IT NOT BE OUTPUTED AS FOUR DIFFERENT INSTANCES OF THE TEST CASE RATHER THAN ONE TEST RESULT?
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger = logGen.loggen() 

    # The time stamp created below is for the screenshots to have unique names 
    # so that if the test fails multiple of times, all of the screenshots will be captured and not be replaced by the next screenshot
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%b_%d_%H:%M:%S_%p")


    # 1. This data driven test "test_login_ddt" will try to log in the nopcommerce page with multple different credentials
    # 2. It uses openpyxl(This framework is stored in utilites/XLUtils.py which has been imported to this file)
    #to read and get data from the TestData/LoginData.xlsx excel sheet file
    # 3. This functions uses a custom logger to store custom logs in Logs/automation.log files
    # 4. This funtion also uses a setup function to set up the enviromnt for the test to run in (ex. Chrome)
    # 5. This function also uses common data used in most test cases
    # 5.1 Common data are stored in Configurations/config.ini
    # 5.2 utilities/readProperties.py file imports Configurations/config.ini file to read and return data from.
    # 5.3 This class uses a ReadConfig.getApplicationURL function from utilities/readProperties.py file to store the returned data to the "baseURL" global variable
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("000000000000000000000000000000000000000000000000")
        self.logger.info("************** Test_002_DDT_Login *************")
        self.logger.info("************** Verifying Login DDT Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")


        # 1. This creates a list[2, 3, 4, 5] because there are 4 rows of data in my excel sheet 
        # 2. In each loop I am storing the values i'm looking for from the excel sheet in variables (ex. self.user, self.password, &etc)
        # 3. After storing my values, I call on my methods in my POM class and pass my stored values from my excel sheet through them (Making this test Data Driven)
        # 4. After Loging in in each loop with different data from the excel sheet, I check if the results are as expected with an if else statement
        # and store "Pass" or "Fail" in a list I created for each loop
        # 5. After my test loop, I check my list of "Pass" or "Fail" and see if there are any "Fail" values.
        # this tells me that a test failed if there are any values in the list equal to "Fail", so this failure makes this whole test a failure 
        for r in range(2,self.rows+1): 
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            lst_status = []
            if act_title == exp_title:
                if self.exp =="Pass":
                    self.logger.info("*** Row {} login data has Passed ***".format(r))
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp =="Fail":
                    self.driver.save_screenshot(".//Screenshots//"+ self.st + "_" +"test_login_ddt.png")
                    self.logger.info("*** Failed (I Logged in with invalid credentials) ***")
                    self.logger.info("*** Row {}, Username: {} Password: {} ***".format(r, self.user, self.password))
                    self.lp.clickLogout()
                    lst_status.append("Fail") 
            elif act_title != exp_title:
                if self.exp =="Pass":
                    self.driver.save_screenshot(".//Screenshots//"+ self.st + "_" +"test_login_ddt.png")
                    self.logger.info("*** Failed (I couldn't log in with these valid credentials) ***")
                    self.logger.info("*** Row {}, Username: {} Password: {} ***".format(r, self.user, self.password))
                    lst_status.append("Fail")
                elif self.exp =="Fail":
                    self.logger.info("*** Row {} login data has Passed ***".format(r))
                    lst_status.append("Pass") 


        if "Fail" not in lst_status:
            self.driver.close()
            self.logger.info("************** Login DDT has passed **************")
            self.logger.info("************** status list: {} **************".format(lst_status))
            assert True
        else: 
            self.driver.close()
            self.logger.error("************** Login DDT has failed **************")
            assert False 

        self.logger.info("********** Completed Test_002_DDT_Login ************")        
                