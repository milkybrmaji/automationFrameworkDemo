import pytest 
from selenium import webdriver 
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from selenium.webdriver.common.by import By
import time
import datetime

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    # The time stamp created below is for the screenshots to have unique names 
    # so that if the test fails multiple of times, all of the screenshots will be captured and not be replaced by the next screenshot
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%b_%d_%H:%M:%S_%p")

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("000000000000000000000000000000000000000000000000")
        self.logger.info("************** Test_004_SearchCustomer *************")
        self.logger.info("************** test_searchCustomerByEmail *************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger.info("************** Logging In **************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("************** Traveling to Customers Page **************")
        self.cp = AddCustomer(self.driver)
        self.cp.clickOnCustomerMenu()
        self.cp.clickOnCustomerPage()

        self.logger.info("************** Searching Customer by Email **************")
        self.scp = SearchCustomer(self.driver)
        self.scp.setEmail("victoria_victoria@nopCommerce.com")
        self.scp.clickSearch()
        time.sleep(5)
        searchResult = self.scp.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        if True == searchResult:
            self.logger.info("************** Searching Customer by Email Successful **************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+self.st+"_"+"test_searchCustomerByEmail.png")
            self.logger.info("************** Searching Customer by Email Not Successful **************")
            self.driver.close()
            assert False  
            
            
                