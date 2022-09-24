import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


class AddCustomer():
    lnk_CustomersMenu_Xpath =  "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_CustomersPage_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"

    btn_Addnew_Xpath = "(//i[@class='fas fa-plus-square'])[1]"

    txtInput_Email_Id = "Email"
    txtInput_Password_Id = "Password"
    txtInput_FirstName_Id = "FirstName"
    txtInput_LastName_Id = "LastName"
    # rdInput = Radio Input, this is an input type
    rdInput_MaleGender_Id = "Gender_Male"
    rdInput_FemaleGender_Id = "Gender_Female"
    dateInput_DOB_Id = "DateOfBirth"
    txtInput_ComapanyName_Id = "Company"
    # cbInput = Check Box Input, this is an input type
    cbInput_IsTaxExempt_Id = "IsTaxExempt"

    listItem_Newsletter_Xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-border-down']//div[@role='listbox']"
    listItem_NewsletterOption1_Xpath ="//li[normalize-space()='Your store name']"
    listItem_NewsletterOption2_Xpath = "//li[normalize-space()='Test store 2']"
    unselectListItem_NewsletterOption1_Xpath = "//span[normalize-space()='Your store name']"
    unselectListItem_NewsletterOption1_Xpath = "//span[normalize-space()='Test store 2']"

    listItem_CustomerRoles_Xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listItem_CustomerRolesOption_Administrators_Xpath = "//li[normalize-space()='Administrators']"
    listItem_CustomerRolesOption_ForumModerators_Xpath = "//li[normalize-space()='Forum Moderators']"
    listItem_CustomerRolesOption_Guests_Xpath = "//li[normalize-space()='Guests']"
    listItem_CustomerRolesOption_Vendors_Xpath = "//li[contains(text(),'Vendors')]"
    listItem_CustomerRolesOption_Registered_Id = "f465e0a0-7879-46ba-b9d2-f1b4e51508c4"
    unselectListItem_CustomerRolesOption_Administrators_Xpath = "(//span[@title='delete'])[2]"
    unselectListItem_CustomerRolesOption_ForumModerators_Xpath = "(//span[@title='delete'])[3]"
    unselectListItem_CustomerRolesOption_Guests_Xpath = "(//span[@title='delete'])[4]"
    unselectListItem_CustomerRolesOption_Vendors_Xpath = "(//span[@title='delete'])[5]"
    unselectListItem_CustomerRolesOption_Registered_Xpath = "//span[@title='delete']"

    dropDown_ManagerofVendors_Xpath = "//select[@id='VendorId']"
    dropDown_ManagerofVendorsOption_NotAVendor_Xpath = "//option[@value='0']"
    dropDown_ManagerofVendorsOption_Vendor1_Xpath = "//option[normalize-space()='Vendor 1']"
    dropDown_ManagerofVendorsOption_Vendor2_Xpath = "//option[normalize-space()='Vendor 2']"

    cbInput_Active_Id = "Active"
    txtInput_AdminComment_Id = "AdminComment"
    btn_Save_Xpath = "//button[@name='save']"
    btn_SaveAndContinueEdit = "//button[normalize-space()='Save and Continue Edit']" 


    # BELOW ARE ONLY SOME FUNCTIONS FOR SOME OF THE VARIABLES ABOVE

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_CustomersMenu_Xpath).click()

    def clickOnCustomerPage(self):
        self.driver.find_element(By.XPATH, self.lnk_CustomersPage_Xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_Addnew_Xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtInput_Email_Id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtInput_Password_Id).send_keys(password)        

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtInput_FirstName_Id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtInput_LastName_Id).send_keys(lname)

    def clickGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdInput_MaleGender_Id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdInput_FemaleGender_Id).click()
        else:
            self.driver.find_element(By.ID, self.rdInput_MaleGender_Id).click()    

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.dateInput_DOB_Id).send_keys(dob)        

    def setCompanyName(self, name):
        self.driver.find_element(By.ID, self.txtInput_ComapanyName_Id).send_keys(name)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.listItem_CustomerRoles_Xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.driver.find_element(By.ID, self.listItem_CustomerRolesOption_Registered_Id).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.listItem_CustomerRolesOption_Administrators_Xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.listItem_CustomerRolesOption_ForumModerators_Xpath).click()
        elif role == "Guests": #Guest and Registered cannot be chosen together, Registered must be unselected here before selecting Guests becuase Registered is selected by default.
            self.driver.find_element(By.XPATH, self.unselectListItem_CustomerRolesOption_Registered_Xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.listItem_CustomerRoles_Xpath).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.listItem_CustomerRolesOption_Guests_Xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.listItem_CustomerRolesOption_Vendors_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.unselectListItem_CustomerRolesOption_Registered_Xpath).click()
            self.driver.find_element(By.XPATH, self.listItem_CustomerRoles_Xpath).click()
            self.driver.find_element(By.XPATH, self.listItem_CustomerRolesOption_Guests_Xpath).click()
        time.sleep(3)

    def setManagerofVendor(self, value):
        self.driver.find_element(By.XPATH, self.dropDown_ManagerofVendors_Xpath).click()
        time.sleep(3)
        if value == "Not a vendor":
            self.driver.find_element(By.XPATH, self.dropDown_ManagerofVendorsOption_NotAVendor_Xpath).click()
        elif value == "Vendor 1":
            self.driver.find_element(By.XPATH, self.dropDown_ManagerofVendorsOption_Vendor1_Xpath).click()
        elif value == "Vendor 2":
            self.driver.find_element(By.XPATH, self.dropDown_ManagerofVendorsOption_Vendor2_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.dropDown_ManagerofVendorsOption_NotAVendor_Xpath).click()            

    def setAdminComment(self, comment):
        self.driver.find_element(By.ID, self.txtInput_AdminComment_Id).send_keys(comment) 

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_Xpath).click()       