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

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    # The time stamp created below is for the screenshots to have unique names 
    # so that if the test fails multiple of times, all of the screenshots will be captured and not be replaced by the next screenshot
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%b_%d_%H:%M:%S_%p")

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        self.logger.info("************** test_searchCustomerByName *************")

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

        self.logger.info("************** Searching Customer by Name **************")
        self.scp = SearchCustomer(self.driver)
        self.scp.setFirstName("Ty")
        self.scp.clickSearch()
        time.sleep(5)
        searchResult = self.scp.searchCustomerByName("Victoria")
        if True == searchResult:
            self.logger.info("************** Searching Customer by Name Successful **************")
            assert True
            self.driver.close()
        else:
            print(searchResult)
            self.driver.save_screenshot(".//Screenshots//"+self.st+"_"+"test_searchCustomerByName.png")
            self.logger.info("************** Searching Customer by Name Not Successful **************")
            self.driver.close()
            assert False