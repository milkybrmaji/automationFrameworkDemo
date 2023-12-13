import pytest
from selenium import webdriver 
from pageObjects
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import time
import datetime

class Test_001_SalesSearch:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    # The time stamp created below is for the screenshots to have unique names 
    # so that if the test fails multiple of times, all of the screenshots will be captured and not be replaced by the next screenshot
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%b_%d_%H:%M:%S_%p")

    #@pytest.mark.regression
    def test_searchAllByDay(self, setup):
        self.logger.info("************** Test_searchAllByDay **************")
        self.logger.info("************** All filters have All selected except group by which has Day selected **************")
        self.driver = setup
        self.driver.get(self.baseURL)
