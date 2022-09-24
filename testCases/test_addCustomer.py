import pytest 
from selenium import webdriver 
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from selenium.webdriver.common.by import By
import string
import random
import time
import datetime


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = logGen.loggen()

    # The time stamp created below is for the screenshots to have unique names 
    # so that if the test fails multiple of times, all of the screenshots will be captured and not be replaced by the next screenshot
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y_%b_%d_%H:%M:%S_%p")

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("000000000000000000000000000000000000000000000000")
        self.logger.info("************** Test_003_AddCustomer *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #I create an instance of my Login Page Object here and use it to log in
        self.logger.info("************** Logging in **************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        #I create an instance of my Add Customer Page Object here and use it to add a new customer
        self.logger.info("************** Going to Customers Page **************")
        self.cp = AddCustomer(self.driver)
        self.cp.clickOnCustomerMenu()
        self.cp.clickOnCustomerPage()

        self.logger.info("************** Adding New Customer **************")
        self.cp.clickOnAddnew()
        # Below I am generating a new email each time I run this test
        self.email = random_generator()+"@gmail.com"
        self.cp.setEmail(self.email) 
        self.cp.setPassword("testtest") 
        self.cp.setFirstName("Milk") 
        self.cp.setLastName("Shake") 
        self.cp.clickGender("Male") 
        self.cp.setDOB("01/07/1990") 
        self.cp.setCompanyName("Shake Land") 
        self.cp.setCustomerRoles("Guests") 
        self.cp.setManagerofVendor("Vendor 2") 
        self.cp.setAdminComment("Testing, testing 1, 2, 3") 
        self.cp.clickSave()
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        if "customer has been added successfully" in self.msg:
            self.logger.info("************** Cutomer Successfully Added **************")
            assert True == True
        else:
            self.driver.save_screenshot(".//Screenshots//"+self.st+"_"+"test_addCustomer_src.png")
            self.logger.error("************** Adding Cutomer not Successful **************")
            assert True == False

        self.driver.close()    

#This function is generating 8 random character letters and numbers. I am using the returned value to create my unique emails in my test case above
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))        