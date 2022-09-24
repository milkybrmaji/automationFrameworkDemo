
import pytest
from selenium import webdriver 
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import time
import datetime

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    # The time stamp created below is for the screenshots to have unique names 
    # so that if the test fails multiple of times, all of the screenshots will be captured and not be replaced by the next screenshot
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%b_%d_%H:%M:%S_%p")

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************** Test_001_Login **************")
        self.logger.info("************** Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Home Page title has passed **************")
        else: 
            # self.shot_title = self.st + "_" + "test_homePageTitle.png"
            self.driver.save_screenshot(".//Screenshots//"+ self.st + "_" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Home Page title has failed **************")
            assert False 
 
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************** Verifying Login **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
    
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************** Login has passed **************")
        else: 
            self.driver.save_screenshot(".//Screenshots//"+ self.st + "_" +"test_login.png")
            self.driver.close()
            self.logger.error("************** Login title has failed **************")
            assert False
       